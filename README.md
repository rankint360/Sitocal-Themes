# Sitocal Themes

Shared theme library for Sitocal. Each theme has its own folder, versioned Netlify deployment and editable source ZIPs, setup guide, variation prompts, and SHA-256 checksums. Source code and artwork are bundled in the editable source ZIPs.

| Theme | Version | Design | Files |
| --- | --- | --- | --- |
| ClearFlow | 1.2.0 | Forest/ivory drain-service design | [ClearFlow](ClearFlow/) |
| Drainora | 1.0.0 | Faithful dark-purple clone of the original template | [Drainora](Drainora/) |
| Copperline | 1.0.0 | Navy/copper, technician photography, inspection-first layout | [Copperline](Copperline/) |
| Pestward | 1.0.0 | Faithful NYC rodent-control clone | [Pestward](Pestward/) |
| Pestward Fieldworks | 1.0.0 | Forest palette with a building sketch and entry-point guide | [Pestward Fieldworks](Pestward-Fieldworks/) |

## Deploy a theme

Download its `*-netlify-deploy-*.zip`, extract it, and upload the extracted directory containing `index.html` to Netlify. The ZIP is already built. For repository-based development, extract the source ZIP and follow that theme's README.

All forms are demos. No forms, bookings, or payments are connected. Hosted preview URLs and screenshots are pending; this repository does not claim completed visual QA or native Sitocal compatibility. See individual guides for verification and importer limitations.

## Future themes and releases

Keep one top-level folder per theme. Preserve older versioned ZIPs when adding a new release; update the theme guide, checksum file and this catalog. Store future preview screenshots in `<Theme>/previews/` and link verified live preview URLs from its README. Do not commit credentials, customer data, build caches or dependencies. These are versioned artifact files, not GitHub Release objects.
