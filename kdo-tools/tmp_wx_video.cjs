// 抓取公众号文章 videoPageInfos
const { chromium } = require('C:/Users/Administrator/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs');

const URLS = [
  ['SPIN大师研究', 'https://mp.weixin.qq.com/s/prY4f9TdJA_Kzu7c0PzNEg'],
  ['SPIN销售法', 'https://mp.weixin.qq.com/s/57qkS_cuEJrg5luz8C1XoQ'],
  ['ICL行业SPIN', 'https://mp.weixin.qq.com/s/2RWJEHSJJI0NS8YKO3da1Q'],
];

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = browser.contexts()[0];
  for (const [name, url] of URLS) {
    const page = await ctx.newPage();
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await page.waitForTimeout(4000);
      const info = await page.evaluate(() => {
        const html = document.body ? document.body.innerText.slice(0, 500) : '';
        const vidText = document.body.innerHTML.match(/<video[^>]*/g) || [];
        // videoPageInfos 通常在 script 里
        const m = document.body.innerHTML.match(/videoPageInfos\s*=\s*(\[.*?\])\s*;/);
        let parsed = null;
        if (m) { try { parsed = JSON.parse(m[1]); } catch(e) { parsed = m[1].slice(0, 300); } }
        return { title: document.title.slice(0, 80), htmlLen: document.body.innerHTML.length,
                 videos: vidText.length, videoInfos: parsed ? JSON.stringify(parsed).slice(0, 500) : 'NO_VIDEOINFOS' };
      });
      console.log(`=== ${name} ===`);
      console.log('TITLE:', info.title);
      console.log('HTML_LEN:', info.htmlLen, 'VIDEO_TAGS:', info.videos);
      console.log('INFOS:', info.videoInfos);
    } catch (e) {
      console.log(`=== ${name} === ERR: ${e.message.slice(0, 150)}`);
    }
    await page.close();
  }
  await browser.close();
})().catch(e => { console.error('FATAL:', e.message); process.exit(1); });
