// 按 listitem 顺序干净提取：每个 listitem 取其下 docx blocks
// 用法: node listitem_extract.cjs <tab_id> <out_json>
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

  // 重置
  await evaluate(`window.scrollTo(0,0); window.__liMap = new Map(); true`);
  await sleep(1500);

  // 采集函数：按 DOM 中 listitem 顺序收集其子 docx 块（避免外层重复）
  const collectExpr = `(() => {
    const seen = window.__liMap || new Map();
    const items = Array.from(document.querySelectorAll('.listitem, [class*="listitem"]'));
    const out = [];
    items.forEach(li => {
      // li 的 item-N id
      const cm = ((li.className)||'').toString().match(/item-(\\d+)/);
      if (!cm) return;
      const n = Number(cm[1]);
      const blocks = Array.from(li.querySelectorAll('.docx-text-block, .docx-heading1-block, .docx-heading2-block, .docx-heading3-block, .docx-heading4-block, .docx-heading5-block, .docx-bullet-block, .docx-ordered-block, .docx-code-block, .docx-quote-block, .docx-callout-block, .docx-divider-block, .docx-file-block, .docx-grid-block, .docx-table-block'));
      if (!blocks.length) return;
      // 该 li 下可能有多个块，但真正的"块列表项"通常是1个主块 + 内部子块
      // 只取直接可见的块（跳过嵌套容器内重复）
      blocks.forEach(b => {
        // 跳过作为别的 block 后代的块（嵌套容器）
        const isNested = b.closest('.docx-callout-block, .docx-quote-block, .docx-table-block, .docx-grid-block') && !b.matches('.docx-callout-block, .docx-quote-block, .docx-table-block, .docx-grid-block');
        if (isNested) return;
        const t = b.innerText || '';
        if (!t || t.length < 1) return;
        const cls = b.className.toString();
        const m = cls.match(/docx-([a-z0-9]+)-block/);
        if (!m) return;
        const k = n + '|' + m[1] + '|' + t.slice(0, 200);
        if (seen.has(k)) return;
        seen.set(k, true);
        out.push({ n, type: m[1], text: t });
      });
    });
    window.__liMap = seen;
    return out;
  })()`;

  const info = await evaluate(`({docH: document.documentElement.scrollHeight, winH: window.innerHeight})`);
  console.log('DOC_H:', info.docH, 'WIN_H:', info.winH);
  const STEP = Math.floor(info.winH * 0.45);
  const totalSteps = Math.ceil(info.docH / STEP) + 3;

  const all = [];
  const seenKeys = new Set();
  let zeroStreak = 0;
  for (let i = 0; i <= totalSteps; i++) {
    await evaluate(`window.scrollTo(0, ${i * STEP}); true`);
    await sleep(900);
    const items = await evaluate(collectExpr);
    let added = 0;
    for (const it of items) {
      const k = it.n + '|' + it.type + '|' + it.text.slice(0, 200);
      if (!seenKeys.has(k)) { seenKeys.add(k); all.push(it); added++; }
    }
    console.log('STEP', i, 'added:', added, 'total:', all.length);
    if (added === 0) { zeroStreak++; if (zeroStreak >= 3) { console.log('BREAK'); break; } }
    else zeroStreak = 0;
  }
  // 底部停留 + 回顶
  await evaluate(`window.scrollTo(0, ${info.docH}); true`);
  await sleep(2000);
  let b = await evaluate(collectExpr);
  b.forEach(it => { const k = it.n + '|' + it.type + '|' + it.text.slice(0, 200); if (!seenKeys.has(k)) { seenKeys.add(k); all.push(it); } });
  console.log('BOTTOM added, total:', all.length);
  await evaluate(`window.scrollTo(0, 0); true`);
  await sleep(1500);
  b = await evaluate(collectExpr);
  b.forEach(it => { const k = it.n + '|' + it.type + '|' + it.text.slice(0, 200); if (!seenKeys.has(k)) { seenKeys.add(k); all.push(it); } });
  console.log('TOP-AGAIN total:', all.length);

  // 按 n 排序输出
  all.sort((a, b) => a.n - b.n);
  // 检查 n 是否有缺口/重复 n 多个块
  const nCounts = {};
  all.forEach(a => { nCounts[a.n] = (nCounts[a.n]||0)+1; });
  const multiN = Object.entries(nCounts).filter(([k,v]) => v > 1).length;
  console.log('FINAL:', all.length, 'unique n:', Object.keys(nCounts).length, 'n with >1 block:', multiN);

  const fs = require('fs');
  fs.writeFileSync(outPath, JSON.stringify(all, null, 1), 'utf-8');
  console.log('SAVED:', outPath);
  ws.close();
  process.exit(0);
}
main().catch(e => { console.log('ERR: ' + e.message); process.exit(1); });
