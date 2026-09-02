// CDP 通用执行器：node cdp_eval.js <tab_id> '<js_expression>'
// 返回 evaluate 结果（JSON）
const tabId = process.argv[2];
const expr = process.argv[3];

async function main() {
  const list = await (await fetch('http://127.0.0.1:9222/json/list')).json();
  const tab = list.find(t => t.id === tabId);
  if (!tab) { console.log('TAB_NOT_FOUND'); process.exit(1); }
  const ws = new WebSocket(tab.webSocketDebuggerUrl);
  await new Promise(res => ws.onopen = res);
  const result = await new Promise((res) => {
    ws.onmessage = (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id === 1) res(msg);
    };
    ws.send(JSON.stringify({
      id: 1,
      method: 'Runtime.evaluate',
      params: { expression: expr, returnByValue: true, awaitPromise: true }
    }));
  });
  ws.close();
  if (result.result && result.result.exceptionDetails) {
    console.log('EXCEPTION: ' + JSON.stringify(result.result.exceptionDetails).slice(0, 500));
    process.exit(1);
  }
  const val = result.result && result.result.result ? result.result.result.value : undefined;
  console.log(typeof val === 'string' ? val : JSON.stringify(val));
}
main().catch(e => { console.log('ERR: ' + e.message); process.exit(1); });
