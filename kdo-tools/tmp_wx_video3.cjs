// 查找公众号 mpvideo 数据变量
const { chromium } = require('C:/Users/Administrator/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs');

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = browser.contexts()[0];
  const page = await ctx.newPage();
  try {
    await page.goto('https://mp.weixin.qq.com/s/prY4f9TdJA_Kzu7c0PzNEg', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(5000);
    const info = await page.evaluate(() => {
      const html = document.body.innerHTML;
      const mpvideoIdx = html.indexOf('mpvideo');
      const mpvideoCtx = mpvideoIdx >= 0 ? html.slice(mpvideoIdx - 100, mpvideoIdx + 500) : 'NO_MPVIDEO';
      // 找 vid / videoPageInfos / url 相关变量
      const vidM = html.match(/[\"']vid[\"']\s*:\s*[\"']([^\"']+)[\"']/) || html.match(/var\s+vid\s*=\s*[\"']([^\"']+)[\"']/);
      const vpiM = html.match(/videoPageInfos[\s\S]{0,800}/);
      const playUrlM = html.match(/https?:\/\/[^\"'\\s]*(mpvideo|vod)[^\"'\\s]*/g);
      return {
        mpvideoCtx: mpvideoCtx.slice(0, 400),
        vid: vidM ? vidM[1] : 'NO_VID',
        vpi: vpiM ? vpiM[0].slice(0, 300) : 'NO_VPI',
        playUrls: playUrlM ? playUrlM.slice(0, 5) : []
      };
    });
    console.log(JSON.stringify(info, null, 1).slice(0, 2500));
  } catch (e) {
    console.log('ERR:', e.message.slice(0, 200));
  }
  await browser.close();
})().catch(e => { console.error('FATAL:', e.message); process.exit(1); });
