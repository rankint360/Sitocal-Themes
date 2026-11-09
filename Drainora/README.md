# Drainora — original theme clone

Drainora is a separate renamed copy of https://theme1-preview.netlify.app/. It is not the ClearFlow redesign.

## Preserved

- All 20 linked pages: home, about, contact, services, locations, ten service detail pages, five location detail pages.
- Original HTML layout, class lists, purple/dark styling, icons, animation styles, images, FAQ and navigation scripts.
- Original copy, including the source template's sample testimonials, statistics and placeholder legal links. Treat all business claims as illustrative demo content, not verified claims.
- Jupiter remains the geographic location; the business/theme brand is Drainora.

## Changes

- Replaced Jupiter Drainers with Drainora in page source, titles, descriptions and visible branding.
- Bundled external Tailwind browser runtime, Animate.css and seven Pexels images locally. Preserved their bytes; no visual redesign.
- Made asset paths root-relative so nested pages work on another host.
- Removed original-host canonical/OG URL tags, LocalBusiness JSON-LD and Netlify injected promotional comment. Set noindex for this mockup.
- Added a demo-only guard for form submits and phone/email actions. Appearance stays the same; interaction reports that nothing was sent/booked.

## Build and deployment

No dependency installation required. Use a modern Node.js runtime:

```
npm run build
npm run check
npm run preview
```

Netlify build command: npm run build. Publish directory: dist. For manual deploy, extract the deploy ZIP and upload its contents, with index.html at the root. No real form, booking or payment service is connected.

Source pages live in source/pages; original CSS and scripts are in source/assets. build.mjs packages these into dist. source/capture.json records original resource URLs and asset integrity hashes. capture.mjs is an optional original-site recapture utility; running it intentionally refreshes the source from the remote template. Normal builds never fetch that site.

The bundled Tailwind browser runtime is retained to match the source; this is not a precompiled Tailwind production conversion. No source repository or original component framework was available: these are editable static page sources.

## Sitocal

dist/theme.json inventories the package. This fidelity-first clone is raw HTML/CSS and is NOT compatible with the ClearFlow portable-document importer without a dedicated adapter. No Sitocal integration is claimed. Maintain its native markup/styles when adding editor mappings.

## Verification and status

Automated verification compares every HTML class list and every downloaded asset hash against captured source, checks local page/asset links, branding and JavaScript syntax. Browser pixel comparison and interaction testing have not been performed for this clone. Netlify publication is pending an authenticated session.

## Two optional variation prompts

1. Create “Drainora Midnight” as a separate drain-cleaning theme variation. Preserve the original section order and page structure; use midnight blue with cyan accents and keep all forms demo-only.
2. Create “Drainora Pearl” as a separate drain-cleaning theme variation. Preserve the original page structure and typography hierarchy; use warm white, charcoal text and violet accents, keeping all forms demo-only.

These prompts are suggestions; this package remains the original purple/dark design.
