// 分段滚动提取 v2：慢速 + 连续3段零新增才break + 到底停留
// 用法: node segmented_extract2.cjs <tab_id> <out_json>
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

  // 重置已见集合
  await evaluate(`window.__seenBlocks = new Set(); window.scrollTo(0,0); true`);
  await sleep(1200);

  const extractExpr = `(() => {
    const seen = window.__seenBlocks || new Set();
    const out = [];
    const blocks = Array.from(document.querySelectorAll('[class*="docx-"]')).filter(b => /docx-(heading\\d+|text|callout|quote|bullet|ordered|code|divider|image|file|mention|grid|column|page)-block/.test(b.className));
    blocks.forEach(b => {
      const m = b.className.match(/docx-([a-z0-9]+)-block/);
      if (!m) return;
      const type = m[1];
      const t = b.innerText || '';
      if (!t || t.length < 1) return;
      const key = type + '|' + t.slice(0, 150);
      if (seen.has(key)) return;
      seen.add(key);
      out.push({ type, text: t });
    });
    window.__seenBlocks = seen;
    return out;
  })()`;

  const all = [];
  const seenKeys = new Set();
  const collect = async (tag) => {
    const items = await evaluate(extractExpr);
    let added = 0;
    for (const it of items) {
      const k = it.type + '|' + it.text.slice(0, 150);
      if (!seenKeys.has(k)) { seenKeys.add(k); all.push(it); added++; }
    }
    console.log(tag, 'added:', added, 'total:', all.length, 'curLen:', (await evaluate('document.body.innerText.length')));
    return added;
  };

  const info = await evaluate(`({docH: document.documentElement.scrollHeight, winH: window.innerHeight})`);
  console.log('DOC_H:', info.docH, 'WIN_H:', info.winH);
  const STEP = Math.floor(info.winH * 0.45);  // 更小步长
  const totalSteps = Math.ceil(info.docH / STEP) + 3;
  let zeroStreak = 0;
  for (let i = 0; i <= totalSteps; i++) {
    await evaluate(`window.scrollTo(0, ${i * STEP}); true`);
    await sleep(900);  // 更长等待
    const added = await collect('STEP ' + i);
    if (added === 0) { zeroStreak++; if (zeroStreak >= 3) { console.log('BREAK at step', i); break; } }
    else zeroStreak = 0;
  }
  // 到底部多停留
  await evaluate(`window.scrollTo(0, ${info.docH}); true`);
  await sleep(2000);
  await collect('BOTTOM');
  // 回顶补一轮
  await evaluate(`window.scrollTo(0, 0); true`);
  await sleep(1500);
  await collect('TOP-AGAIN');

  console.log('FINAL_TOTAL:', all.length);
  const fs = require('fs');
  fs.writeFileSync(outPath, JSON.stringify(all, null, 1), 'utf-8');
  console.log('SAVED:', outPath);
  ws.close();
  process.exit(0);
}
main().catch(e => { console.log('ERR: ' + e.message); process.exit(1); });
