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

## 2026-04-23 — V2 Signature (EPlug + Energy Plus)

### Figma Design
- Source: file `GXUObJIRiX2EfkOujCyNIq`, node `4700:912` (Signature V2)
- New layout: left text block + right column with two stacked logo blocks
- Colors: magenta `#FF00C5` (left + top-right), dark green `#1C4523` (bottom-right)
- Gap between all three blocks: 4px
- Total height: 212px, right column width: 174px

### Content Changes vs V1
- Job title split onto two lines: "Head of EV" / "EPlug • Energy Plus"
- Removed website row (globe icon + `eplug.com`) from left contacts — now only Phone, Email, LinkedIn
- Added "eplug.com" link under EPlug logo (top-right block)
- Added second brand block with Energy Plus logo + "energyplusny.com" link

### Assets
- Exported new logos from Figma as SVG, rendered to transparent PNG via Chrome headless at @2x:
  - `public/assets/images/eplug-logo-v2.png` (284×103) — new EPlug logo with "it's faster" tag
  - `public/assets/images/energyplus-logo.png` (242×86) — Energy Plus wordmark + leaf mark
- Reused existing contact icons from V1 (phone, email, linkedin)

### HTML (`signature-v2.html`)
- Email-safe table layout, inline CSS, `max-width:520px; width:100%`
- Right column uses nested table with 4px spacer row between logo blocks
- Heights balanced via `height:100%` on right inner table so both columns match
- All images use absolute `https://chife-mod.github.io/...` URLs
- Verified via Chrome headless screenshot — 1:1 match with Figma design

### Files Created
- `signature-v2.html` — V2 signature (new primary)
- `public/assets/images/eplug-logo-v2.png`
- `public/assets/images/energyplus-logo.png`

### Decisions
- Kept `max-width:520px` — full-width stretch would inflate the left pink block disproportionately since the right column is fixed at 174px; email-client best practice is 500–600px anyway
- PNG over SVG — Gmail does not render inline/remote SVG reliably

---

## 2026-07-10 — V3 Signature (light layout, Michael Elhav)

### Figma Design
- Source: file `GXUObJIRiX2EfkOujCyNIq`, node `4869:509` (Michael Elhav)
- New light layout: white left panel (name/title/brands/contacts), `#FDFDFD` right panel with vertical divider + two stacked logos
- Frame: 462×194; left panel 284px (padding 24), right panel 178px
- Colors: Eplug brand text `#2E0054`, Energy Plus text `#327A39`, dividers = black 20% → `#CCCCCC`
- Typography: Arial — name 24px bold, everything else 14px, job title uppercase

### Assets (@4x PNG via Figma MCP `download_assets`)
- `chip-phone-v3.png`, `chip-globe-v3.png`, `chip-linkedin-v3.png` (72×72, display 18×18) — circular icon chips with green border baked in (border-radius unreliable in email clients)
- `eplug-logo-v3.png` (520×190, display 130×47) — pink Eplug logo with "It's faster"
- `energyplus-logo-v3.png` (520×186, display 130×46) — green Energy Plus logo
- Logos exported separately (not as one frame) so each carries its own link

### HTML (`signature-v3.html`)
- Email-safe table layout, inline CSS, `width:100%; max-width:462px`
- Vertical panel divider: 1px td with inner div `height:146px`, vertically centered
- Links: `tel:+18444437584,,102`, eplug.com, energyplusny.com, LinkedIn, both logos clickable
- Verified in Chrome preview: table renders exactly 462×194, 1:1 vs Figma screenshot
- Mobile check (375px): no viewport meta → renders at 980 virtual width and scales, same as mobile mail clients; no overflow

### Files Created
- `signature-v3.html` — V3 signature (new primary)
- `public/assets/images/*-v3.png` — five new assets

---
