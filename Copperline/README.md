# Copperline

Premium drain-cleaning and sewer-care theme. A separate variation with navy, copper, warm paper backgrounds, technician photography, editorial typography, numbered service rows and inspection-focused content. No visitor-facing AI or builder attribution.

## Included

- 22 pages: home, about, services index, ten service pages, locations index, five location pages, contact, privacy information and demo terms.
- Custom 404 page; accessible mobile menu; symptom selector; native FAQ disclosures; labeled demo form with browser validation and status confirmation.
- Locally bundled photography, CSS, JavaScript and favicon. No runtime CDN dependencies or package installation.
- theme.json content and static sitocal-theme.json inventory with section hooks and file hashes. This requires a native Sitocal adapter; no existing proprietary editor compatibility is claimed.

## Netlify

Manual deployment: extract copperline-netlify-deploy-v1.0.zip. Upload the extracted folder containing index.html. It already contains generated HTML and assets; no build is necessary.

Repository deployment: extract the source ZIP. Build command: npm run build. Publish directory: dist. netlify.toml contains these settings.

## Local development

Use a modern Node.js runtime. No npm install is needed.

```
npm run build
npm run check
npm run preview
```

Open the local URL printed by the preview server. Root-relative page/asset paths require an HTTP server, not file://.

Edit service data and locations in theme.json, page layouts/copy in build.mjs, design tokens/layout in styles.css, and interactions in app.js. Rebuild after changes. The generated dist folder can be deployed independently. The portable document importer used by ClearFlow is not bundled with this theme.

## Demo behavior

The business is illustrative. There are no invented ratings, testimonials, awards or experience statistics. The photograph is stock imagery, not an actual Copperline employee. Forms never send or store details, take payments or book appointments. Draft indexing is disabled through robots metadata and hosting headers.

Replace sample information and legal content with real business details before a real launch. Live service integrations and publishing were not requested for this delivery.

## Photography

Photo: “Plumber Repairing Pipe with Wrench Indoors” by Bulat843 on Pexels.
Source: https://www.pexels.com/photo/plumber-repairing-pipe-with-wrench-indoors-32588548/
Download: https://images.pexels.com/photos/32588548/pexels-photo-32588548.jpeg?auto=compress&cs=tinysrgb&w=1600
License: https://www.pexels.com/license/
The image is bundled at assets/technician.jpg. No claim of endorsement or employment is made. CSS crops and desaturates it for presentation; the downloaded file is unmodified.

## Verification

Automated checks cover all page links, asset hashes, section anchors, branding, menu and Escape handling, all symptom selector choices, and the demo submit handler. Browser pixel/layout and live interaction verification remain uncompleted because the available browser capture tool could not accept the exposed capture configuration. Responsive CSS targets narrow/mobile and desktop widths, but that is not a substitute for browser verification.

## Two next variation prompts

1. Copperline Estate: Create a residential drain-inspection variation with warm ivory pages, deep navy typography, restrained copper rules, larger property-care photography and a compact inspection-request panel. Preserve service routes and demo-only behavior.
2. Copperline Commercial: Create a commercial drain-maintenance variation with navy backgrounds, copper section numbering, a maintenance-scope table, kitchen/restaurant service content and an inspection-led request flow. Preserve customer data and keep bookings and payments disconnected.
