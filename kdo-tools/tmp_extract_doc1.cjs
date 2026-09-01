// DOC1: Live260：AI口喷基本功内测 candy
const { chromium } = require('C:/Users/Administrator/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright-core/index.mjs');
const fs = require('fs');

const OUT = 'C:/Users/Administrator/Desktop/wiki/00_inbox/Live260-AI口喷基本功内测candy_v5.json';
const TARGET_URL = 'https://yitang.top/fs-doc/d942dd39331738382bd8ecf0ffacbceb/YTJgdq3idoRKwExETDqc5JlfnNd?_uds=hyyy_biu';
const DOC_ID = 'YTJgdq3idoRKwExETDqc5JlfnNd';

(async () => {
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const ctx = browser.contexts()[0];
  const pages = ctx.pages();
  let page = pages.find(p => p.url().includes(DOC_ID));
  if (!page) {
    page = await ctx.newPage();
    await page.goto(TARGET_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(6000);
  }
  await page.bringToFront();
  console.log('CURRENT_URL:', page.url().slice(0, 150));
  console.log('TITLE:', (await page.title()).slice(0, 100));
  const bodyLen = await page.evaluate(() => document.body.innerText.length);
  console.log('BODY_LEN:', bodyLen);
  const loginWall = await page.evaluate(() => document.body.innerText.includes('扫码登录') || document.body.innerText.includes('微信扫一扫'));
  console.log('LOGIN_WALL:', loginWall);

  // ① 探测滚动容器
  const info = await page.evaluate(() => {
    const scrollables = Array.from(document.querySelectorAll('*')).filter(el =>
      el.scrollHeight > el.clientHeight + 100).map(el => ({
        tag: el.tagName, cls: (el.className || '').toString().slice(0, 60),
        scrollH: el.scrollHeight, clientH: el.clientHeight
      }));
    return {
      scrollables,
      winScrollH: document.documentElement.scrollHeight,
      winClientH: window.innerHeight
    };
  });
  console.log('SCROLLABLES:', JSON.stringify(info.scrollables.slice(0, 10), null, 1));
  console.log('WINDOW:', info.winScrollH, '/', info.winClientH);

  const STEP = Math.floor(info.winClientH * 0.6);
  const totalSteps = Math.ceil(info.winScrollH / STEP) + 2;
  console.log(`STEP=${STEP}, TOTAL_STEPS=${totalSteps}`);

  const seen = new Set();
  const allBlocks = [];

  async function extractVisible() {
    return await page.evaluate(() => {
      const blocks = Array.from(document.querySelectorAll('[class*="docx-"]'))
        .filter(b => b.className.indexOf('block docx-') >= 0);
      return blocks.map(b => {
        const m = b.className.match(/docx-([a-z0-9]+)-block/);
        const type = m ? m[1] : 'unknown';
        return { type, text: (b.innerText || '').trim() };
      }).filter(x => x.text.length > 0);
    });
  }

  function addBlocks(blocks) {
    let added = 0;
    for (const b of blocks) {
      const key = b.type + '|' + b.text.slice(0, 200);
      if (!seen.has(key)) { seen.add(key); allBlocks.push(b); added++; }
    }
    return added;
  }

  let added = addBlocks(await extractVisible());
  console.log(`[0] top blocks=${allBlocks.length} (+${added})`);

  for (let i = 1; i <= totalSteps; i++) {
    await page.evaluate((step) => window.scrollTo(0, step), i * STEP);
    await page.waitForTimeout(700);
    added = addBlocks(await extractVisible());
    console.log(`[${i}] y=${i * STEP} blocks=${allBlocks.length} (+${added})`);
    if (i % 10 === 0) fs.writeFileSync(OUT, JSON.stringify({ info, allBlocks }, null, 1), 'utf-8');
  }

  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1000);
  added = addBlocks(await extractVisible());
  console.log(`[bottom] blocks=${allBlocks.length} (+${added})`);

  fs.writeFileSync(OUT, JSON.stringify({ info, allBlocks }, null, 1), 'utf-8');
  console.log('SAVED:', OUT, 'TOTAL_BLOCKS:', allBlocks.length);
  await browser.close();
})().catch(e => { console.error('FATAL:', e.message); process.exit(1); });
