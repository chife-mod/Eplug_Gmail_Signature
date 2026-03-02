# Project History Log

**Project Overview:**  
EPlug Gmail Signature — HTML email signature for Gmail, based on a Figma design. The project produces a table-based, inline-styled HTML signature that is compatible with Gmail, Outlook, Apple Mail, and mobile clients. Assets (icons, logo) are hosted on GitHub Pages (`chife-mod.github.io`). The signature features a magenta (#FF00C5) background, white text (Arial), contact icons exported from Figma as @2x PNGs, and the EPlug logo.

---

## 2026-03-02 — Initial creation of Gmail HTML Signature

### Figma Design Analysis
- Inspected Figma file `NsarAMa9SQMVyRCQDvgqg3`, node `296:197` (Email Signature)
- Extracted design specs: padding 24px, name 20px bold, text 14px, icons 18×18, logo 176×64
- Background color: `#FF00C5` (magenta)
- Font: Arial, white (`#FFFFFF`)
- Two-column layout: contacts left, logo right

### Asset Export
- Exported assets via Figma Images API (`/v1/images/`) using `scripts/export-figma-frame.js`
- Assets exported @2x PNG: `eplug-logo.png`, `icon-phone.png`, `icon-email.png`, `icon-linkedin.png`, `icon-globe.png`, `signature-full.png`
- Removed hardcoded Figma token from `export-figma-frame.js` — now uses `FIGMA_TOKEN` env variable only
- Cleaned up SVG intermediates (replaced with PNGs for Gmail compatibility)

### HTML Signature (`signature-live.html`)
- Built fully coded HTML signature with table-based layout and all inline styles
- `width:100%; max-width:520px` — responsive within Gmail's constraints
- Solid `#FF00C5` background (Gmail strips `background-image`)
- Contact rows with Figma-exported PNG icons from GitHub Pages
- Logo pinned to right column
- All links clickable: `tel:`, `mailto:`, LinkedIn, website
- Images hosted on GitHub Pages: `https://chife-mod.github.io/Eplug_Gmail_Signature/public/assets/images/`

### Image-based Variant (`signature.html`)
- Created alternative image-based signature using `signature-full.png` (pixel-perfect Figma export)
- Hidden accessible links underneath the image
- Useful as fallback for maximum visual consistency

### Infrastructure
- Initialized Git repository, pushed to `https://github.com/chife-mod/Eplug_Gmail_Signature`
- Enabled GitHub Pages (Deploy from branch: `main`, root)
- Verified assets accessible via `https://chife-mod.github.io/...` (HTTP 200, `content-type: image/png`)
- Created `.gitignore` (`.env`, `node_modules/`)
- Removed Figma token from `.agents/figma-export-guide.md` (GitHub Push Protection blocked the push with hardcoded token)

### Preview & Testing
- Created `index.html` — preview page showing both signature variants
- Created `signature-test.html` — local test version with relative paths
- Tested in Gmail Web (personal): background, text, icons render correctly
- Tested in Gmail Workspace (corporate): signature renders as plain text — likely Workspace admin restriction
- Identified Gmail limitations: `background-image` stripped, `border-radius` stripped, SVGs/base64 not supported

### Files Created
- `signature-live.html` — main HTML signature (recommended)
- `signature.html` — image-based fallback
- `signature-test.html` — local preview version
- `index.html` — preview page with both variants
- `README.md` — installation instructions
- `scripts/export-figma-frame.js` — Figma asset export script
- `public/assets/images/` — all PNG assets (@2x)

---
