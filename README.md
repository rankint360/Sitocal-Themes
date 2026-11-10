# Sitocal Themes

Shared theme library for Sitocal. Each theme has its own folder, versioned Netlify deployment and editable source ZIPs, setup guide, variation prompts, and SHA-256 checksums. Source code and artwork are bundled in the editable source ZIPs.

| Theme | Version | Design | Files |
| --- | --- | --- | --- |
| ClearFlow | 1.3.0 | Forest/ivory drain-service design | [ClearFlow](ClearFlow/) |
| Drainora | 1.1.0 | Faithful dark-purple clone of the original template | [Drainora](Drainora/) |
| Copperline | 1.1.0 | Navy/copper, technician photography, inspection-first layout | [Copperline](Copperline/) |
| Pestward | 1.1.0 | Faithful NYC rodent-control clone | [Pestward](Pestward/) |
| Pestward Fieldworks | 1.1.0 | Forest palette with a building sketch and entry-point guide | [Pestward Fieldworks](Pestward-Fieldworks/) |
| Trackstead | 1.1.0 | Pueblo garage-door reference clone | [Trackstead](Trackstead/) |
| Trackstead Forge | 1.1.0 | Charcoal and copper garage-door troubleshooting | [Trackstead Forge](Trackstead-Forge/) |
| Canopy Harbor | 1.1.0 | Miami general pest-control reference clone | [Canopy Harbor](Canopy-Harbor/) |
| Canopy Harbor Habitat | 1.1.0 | Teal and citrus pest inspection guide | [Canopy Harbor Habitat](Canopy-Harbor-Habitat/) |
| Tidewell Plumbing | 1.1.0 | Naples plumbing reference clone | [Tidewell Plumbing](Tidewell-Plumbing/) |
| Tidewell Service Desk | 1.1.0 | Plum and sand plumbing service guide | [Tidewell Service Desk](Tidewell-Service-Desk/) |
| SlabTrace | 1.1.0 | Baltimore slab-leak reference clone | [SlabTrace](SlabTrace/) |
| SlabTrace Survey | 1.1.0 | Slate and amber leak inspection guide | [SlabTrace Survey](SlabTrace-Survey/) |
| Jetbrook | 1.1.0 | Jupiter drain-cleaning reference clone | [Jetbrook](Jetbrook/) |
| Jetbrook Linecheck | 1.1.0 | Drain diagnostics with a pipe-route sketch | [Jetbrook Linecheck](Jetbrook-Linecheck/) |
| DuneShield | 1.1.0 | Naples household pest-control reference clone | [DuneShield](DuneShield/) |
| DuneShield Courtyard | 1.1.0 | Olive and sand household inspection guide | [DuneShield Courtyard](DuneShield-Courtyard/) |
| CivicBastion | 1.1.0 | Los Angeles pest-management reference clone | [CivicBastion](CivicBastion/) |
| CivicBastion Routebook | 1.1.0 | Indigo visit-planning and access guide | [CivicBastion Routebook](CivicBastion-Routebook/) |
| Palmetto Ledger | 1.1.0 | Naples property pest-control reference clone | [Palmetto Ledger](Palmetto-Ledger/) |
| Palmetto Ledger Steward | 1.1.0 | Plum property prevention and recurring checks | [Palmetto Ledger Steward](Palmetto-Ledger-Steward/) |
| Carrygrove Moving | 1.1.0 | Austin moving reference clone | [Carrygrove Moving](Carrygrove-Moving/) |
| Carrygrove Roomplan | 1.1.0 | Warm neutrals with room inventory and loading guide | [Carrygrove Roomplan](Carrygrove-Roomplan/) |
| Rillstead Restoration | 1.1.0 | Springfield water damage reference clone | [Rillstead Restoration](Rillstead-Restoration/) |
| Rillstead Drybook | 1.1.0 | Teal drying record and room assessment guide | [Rillstead Drybook](Rillstead-Drybook/) |
| Redbank Recovery | 1.1.0 | Austin water damage reference clone | [Redbank Recovery](Redbank-Recovery/) |
| Redbank Incident Desk | 1.1.0 | Burgundy incident timeline and crew handoff | [Redbank Incident Desk](Redbank-Incident-Desk/) |
| Cascade Junction Plumbing | 1.1.0 | Seattle plumbing reference clone | [Cascade Junction Plumbing](Cascade-Junction-Plumbing/) |
| Cascade Junction Fixture Desk | 1.1.0 | Slate and brass with a fixture symptom guide | [Cascade Junction Fixture Desk](Cascade-Junction-Fixture-Desk/) |

The photo refresh adds credited, locally bundled Pexels imagery to home, service and location pages. See the [audit notes](PHOTO-AUDIT.md) for the fixes and browser-check scope.

## Deploy a theme

Download its `*-netlify-deploy-*.zip`, extract it, and upload the extracted directory containing `index.html` to Netlify. The ZIP is already built. For repository-based development, extract the source ZIP and follow that theme's README.

All forms are demos. No forms, bookings, or payments are connected. Hosted preview URLs and screenshots are pending; this repository does not claim completed visual QA or native Sitocal compatibility. See individual guides for verification and importer limitations.

## Future themes and releases

Keep one top-level folder per theme. Preserve older versioned ZIPs when adding a new release; update the theme guide, checksum file and this catalog. Store future preview screenshots in `<Theme>/previews/` and link verified live preview URLs from its README. Do not commit credentials, customer data, build caches or dependencies. These are versioned artifact files, not GitHub Release objects.
