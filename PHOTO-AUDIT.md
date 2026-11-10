# Theme photo and layout audit

All 29 themes have a refreshed deployment and editable source ZIP in their existing folders. ClearFlow is version 1.3.0. The other 28 are version 1.1.0. Each folder has release notes and SHA-256 checksums.

- Added stock-photo sections to 440 home, service and location pages. Each photo has alternate text and a Pexels credit. The source URLs are also recorded in the site’s assets/pexels/sources.json.
- Repaired broken image references in Jetbrook, Jetbrook Linecheck, DuneShield and DuneShield Courtyard. Fixed early page-script access to the body in the DuneShield and SlabTrace pairs.
- Repaired article contents links in the SlabTrace and Tidewell pairs and corrected the process link on the CivicBastion About pages.
- Contained decorative section overflow on the Pestward and Pestward Fieldworks homepages.

Static local-link and asset checks covered 631 HTML files. Chromium loaded 286 sampled pages across the full library at 390 px and 1440 px widths. The sampled loads finished without missing local requests, uncaught page errors or page-level horizontal overflow. This is a sampled browser audit. ClearFlow also passed its portable-document and saved-project rebuild tests.

The refreshed editable ZIPs contain HTML, styles and local assets under site/. ClearFlow includes its portable document export tooling. Earlier source releases remain in their theme folders.

Photo terms are available in the [Pexels license](https://www.pexels.com/license/).
