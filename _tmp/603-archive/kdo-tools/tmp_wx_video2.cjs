// 提取公众号 video 标签详情
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
        const vids = Array.from(document.querySelectorAll('video'));
        return vids.map(v => {
          const src = v.src || v.currentSrc || '';
          const sources = Array.from(v.querySelectorAll('source')).map(s => s.src).filter(Boolean);
          return {
            src: src.slice(0, 200),
            sources: sources.slice(0, 2).map(s => s.slice(0, 200)),
            outerLen: v.outerHTML.length,
            outerHTML: v.outerHTML.slice(0, 600)
          };
        });
      });
      console.log(`=== ${name} ===`);
      console.log(JSON.stringify(info, null, 1).slice(0, 1200));
    } catch (e) {
      console.log(`=== ${name} === ERR: ${e.message.slice(0, 150)}`);
    }
    await page.close();
  }
  await browser.close();
})().catch(e => { console.error('FATAL:', e.message); process.exit(1); });
