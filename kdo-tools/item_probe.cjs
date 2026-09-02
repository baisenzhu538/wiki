// 精确提取带 item 序号：确认模板重复来自源文档还是提取bug
// 用法: node item_probe.cjs <tab_id>
const tabId = process.argv[2];
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const list = await (await fetch('http://127.0.0.1:9222/json/list')).json();
  const tab = list.find(t => t.id === tabId);
  if (!tab) { console.log('TAB_NOT_FOUND'); process.exit(1); }
  const ws = new WebSocket(tab.webSocketDebuggerUrl);
  await new Promise(res => ws.onopen = res);
  let msgId = 0;
  const pending = {};
  ws.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending[msg.id]) { pending[msg.id](msg); delete pending[msg.id]; }
  };
  const send = (method, params = {}) => new Promise(res => {
    const id = ++msgId;
    pending[id] = res;
    ws.send(JSON.stringify({ id, method, params }));
  });
  const evaluate = async (expression) => {
    const r = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    if (r.result && r.result.exceptionDetails) throw new Error(JSON.stringify(r.result.exceptionDetails).slice(0, 300));
    return r.result.result.value;
  };

  await evaluate(`window.scrollTo(0,0); window.__itemSeen = {}; true`);
  await sleep(1000);

  const collectExpr = `(() => {
    const out = [];
    const blocks = Array.from(document.querySelectorAll('[class*="docx-"]')).filter(b => /docx-(heading\\d+|text|callout|quote|bullet|ordered|code|divider)-block/.test(b.className));
    blocks.forEach(b => {
      const m = b.className.match(/docx-([a-z0-9]+)-block/);
      if (!m) return;
      const t = b.innerText || '';
      if (t.length < 1) return;
      // 找祖先 item-N
      let item = '';
      let el = b.parentElement;
      while (el && el !== document.body) {
        const c = (el.className || '').toString();
        const im = c.match(/item-(\\d+)/);
        if (im) { item = 'item-' + im[1]; break; }
        el = el.parentElement;
      }
      out.push({ type: m[1], item, head: t.slice(0, 60), text: t });
    });
    return out;
  })()`;

  const docH = await evaluate('document.documentElement.scrollHeight');
  const winH = await evaluate('window.innerHeight');
  const STEP = Math.floor(winH * 0.5);
  const totalSteps = Math.ceil(docH / STEP) + 3;

  const allItems = new Map(); // key: type|head|item
  for (let i = 0; i <= totalSteps; i++) {
    await evaluate(`window.scrollTo(0, ${i * STEP}); true`);
    await sleep(900);
    const items = await evaluate(collectExpr);
    items.forEach(it => {
      const k = `${it.item}|${it.type}|${it.text}`;
      if (!allItems.has(k)) allItems.set(k, it);
    });
  }
  await evaluate(`window.scrollTo(0, ${docH}); true`);
  await sleep(1500);
  const bot = await evaluate(collectExpr);
  bot.forEach(it => { const k = `${it.item}|${it.type}|${it.text}`; if (!allItems.has(k)) allItems.set(k, it); });

  // 分析：白皮书标题出现在哪些 item
  const vals = Array.from(allItems.values());
  const wps = vals.filter(v => v.text.includes('Agent 工作白皮书') && v.type === 'heading1');
  const h1 = vals.filter(v => v.type === 'heading1');
  const itemSet = new Set(vals.map(v => v.item));
  const itemCounts = {};
  vals.forEach(v => { itemCounts[v.item] = (itemCounts[v.item]||0)+1; });

  console.log('TOTAL_BLOCKS:', vals.length);
  console.log('ITEM_COUNT:', itemSet.size, 'ITEMS:', Array.from(itemSet).sort((a,b)=>Number(a.split('-')[1])-Number(b.split('-')[1])).join(','));
  console.log('H1_COUNT:', h1.length, 'H1:', h1.map(h=>h.item+'|'+h.text.slice(0,50)));
  console.log('白皮书标题:', wps.map(w=>w.item+'|'+w.head));
  ws.close();
  process.exit(0);
}
main().catch(e => { console.log('ERR: ' + e.message); process.exit(1); });
