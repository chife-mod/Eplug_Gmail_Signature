#!/usr/bin/env node
/**
 * Export a single Figma node as SVG or PNG.
 * Usage: node scripts/export-figma-frame.js <file_key> <node_id> <output_name> <format> [scale]
 */
const https = require('https');
const fs = require('fs');
const path = require('path');

const FIGMA_TOKEN = process.env.FIGMA_TOKEN;
if (!FIGMA_TOKEN) {
  console.error('Error: FIGMA_TOKEN env variable is required. Run: export FIGMA_TOKEN="figd_..."');
  process.exit(1);
}

const FILE_KEY = process.argv[2];
const NODE_ID = (process.argv[3] || '').replace(/-/g, ':');
const NAME = process.argv[4];
const FORMAT = process.argv[5] || 'png';
const SCALE = parseInt(process.argv[6] || '2', 10);

if (!FILE_KEY || !NODE_ID || !NAME) {
  console.error('Usage: node scripts/export-figma-frame.js <file_key> <node_id> <output_name> <format> [scale]');
  process.exit(1);
}

const OUT_DIR = FORMAT === 'svg' ? 'public/assets/icons' : 'public/assets/images';

function get(url, hdrs) {
  return new Promise((ok, fail) => {
    https.get(url, { headers: hdrs }, res => {
      let d = ''; res.on('data', c => d += c);
      res.on('end', () => res.statusCode === 200 ? ok(d) : fail(new Error('HTTP ' + res.statusCode + ': ' + d)));
    }).on('error', fail);
  });
}

function download(url, out) {
  return new Promise((ok, fail) => {
    https.get(url, res => {
      if (res.statusCode !== 200) { fail(new Error('HTTP ' + res.statusCode)); return; }
      const s = fs.createWriteStream(out); res.pipe(s);
      s.on('finish', () => { s.close(); ok(); }); s.on('error', fail);
    }).on('error', fail);
  });
}

(async () => {
  const params = new URLSearchParams({ ids: NODE_ID, format: FORMAT, scale: String(SCALE) });
  const apiUrl = 'https://api.figma.com/v1/images/' + FILE_KEY + '?' + params;
  console.log(`Exporting ${NAME} (${FORMAT} @${SCALE}x) from ${FILE_KEY} node ${NODE_ID}...`);

  const raw = await get(apiUrl, { 'X-Figma-Token': FIGMA_TOKEN });
  const data = JSON.parse(raw);
  const href = data.images?.[NODE_ID];
  if (!href) throw new Error('No URL returned. Response: ' + raw);

  const ext = FORMAT === 'svg' ? '.svg' : '.png';
  const outPath = path.join(OUT_DIR, NAME + ext);
  fs.mkdirSync(path.dirname(outPath), { recursive: true });

  if (FORMAT === 'svg') {
    fs.writeFileSync(outPath, await get(href, {}), 'utf8');
  } else {
    await download(href, outPath);
  }
  console.log(`  ✅ ${outPath}`);
})().catch(e => { console.error('Error:', e.message); process.exit(1); });
