// 分段滚动提取：connect CDP → 分段滚动 → 去重累积 docx blocks → 存 JSON
// 用法: node segmented_extract.cjs <tab_id> <out_json>
const tabId = process.argv[2];
const outPath = process.argv[3];

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

  // ① 检测登录墙
  const loginWall = await evaluate(`/login|扫码登录/.test(document.body.innerText.slice(0,300))`);
  if (loginWall) { console.log('LOGIN_WALL'); process.exit(2); }

  // ② 探测滚动容器（window or element）
  const scrollInfo = await evaluate(`(() => {
    const scrollables = Array.from(document.querySelectorAll('*')).filter(el => el.scrollHeight > el.clientHeight + 100);
    const winH = window.innerHeight, docH = document.documentElement.scrollHeight;
    const useWindow = docH > winH + 100;
    const el = useWindow ? null : (scrollables.sort((a,b)=>b.scrollHeight-a.scrollHeight)[0] || null);
    return { useWindow, winH, docH, elScrollH: el ? el.scrollHeight : 0, elClientH: el ? el.clientHeight : 0, elCls: el ? el.className.toString().slice(0,80) : '' };
  })()`);
  console.log('SCROLL_INFO:', JSON.stringify(scrollInfo));

  // ③ 提取可视区 blocks 的 JS 函数（去重由外层做）
  const extractBlocksExpr = `(() => {
    const seen = window.__seenBlocks || new Set();
    const out = [];
    const blocks = Array.from(document.querySelectorAll('[class*="docx-"]')).filter(b => /docx-(heading\\d+|text|callout|quote|bullet|ordered|code|divider|table|image|file|mention|grid|column|page)-block/.test(b.className));
    blocks.forEach(b => {
      const cls = b.className.toString();
      const m = cls.match(/docx-([a-z0-9]+)-block/);
      if (!m) return;
      const type = m[1];
      const t = b.innerText || '';
      if (!t || t.length < 1) return;
      // 跳过内部嵌套容器（外层容器会重复）
      const key = type + '|' + t.slice(0, 150);
      if (seen.has(key)) return;
      seen.add(key);
      out.push({ type, text: t });
    });
    window.__seenBlocks = seen;
    return { count: out.length, items: out };
  })()`;

  // ④ 滚动到顶开始
  await evaluate(`window.scrollTo(0,0); true`);
  await sleep(800);
  const all = [];
  const seenKeys = new Set();
  const collect = async () => {
    const r = await evaluate(extractBlocksExpr);
    let added = 0;
    for (const it of r.items) {
      const k = it.type + '|' + it.text.slice(0, 150);
      if (!seenKeys.has(k)) { seenKeys.add(k); all.push(it); added++; }
    }
    return { newCount: r.count, total: all.length, added };
  };

  // 初始 + 分段滚动
  let first = await collect();
  console.log('INITIAL:', JSON.stringify(first));

  const { useWindow, winH, docH, elScrollH, elClientH } = scrollInfo;
  if (useWindow) {
    const STEP = Math.floor(winH * 0.6);
    const totalSteps = Math.ceil(docH / STEP) + 2;
    for (let i = 1; i <= totalSteps; i++) {
      await evaluate(`window.scrollTo(0, ${i * STEP}); true`);
      await sleep(600);
      const r = await collect();
      console.log('STEP', i, 'added:', r.added, 'total:', r.total);
      if (r.added === 0 && r.newCount === 0) break;
    }
  } else {
    // element 容器滚动：需先找到容器引用，用 JS 内部循环
    console.log('ELEMENT_CONTAINER_MODE — 用 JS 内循环');
    const expr = `(async () => {
      const sleep2 = ms => new Promise(r => setTimeout(r, ms));
      const scrollables = Array.from(document.querySelectorAll('*')).filter(el => el.scrollHeight > el.clientHeight + 100);
      const container = scrollables.sort((a,b)=>b.scrollHeight-a.scrollHeight)[0];
      const STEP = Math.floor(container.clientHeight * 0.6);
      const total = Math.ceil(container.scrollHeight / STEP) + 2;
      for (let i = 1; i <= total; i++) {
        container.scrollTop = i * STEP;
        await sleep2(500);
      }
      window.scrollTo(0, 999999);
      await sleep2(800);
      return 'scrolled_to_bottom';
    })()`;
    await evaluate(expr);
    await collect();
    // 回顶部反向再来一次确保全覆盖
    await evaluate(`(() => { const c = Array.from(document.querySelectorAll('*')).filter(el => el.scrollHeight > el.clientHeight + 100).sort((a,b)=>b.scrollHeight-a.scrollHeight)[0]; if(c){ c.scrollTop = 0; } window.scrollTo(0,0); return true; })()`);
    await sleep(500);
  }

  // ⑤ 回顶兜底提取一次
  await evaluate(`window.scrollTo(0,0); true`);
  await sleep(600);
  await collect();

  console.log('FINAL_TOTAL:', all.length);
  // 写入文件（node 端直接写）
  const fs = require('fs');
  fs.writeFileSync(outPath, JSON.stringify(all, null, 1), 'utf-8');
  console.log('SAVED:', outPath);
  ws.close();
  process.exit(0);
}
main().catch(e => { console.log('ERR: ' + e.message); process.exit(1); });
