# ClearFlow

Version 1.3.0 adds credited Pexels photos on 18 pages. The photos illustrate the service or property type.

## Deploy

Extract the deployment ZIP and upload the directory containing index.html. For Cloudflare Pages Git builds, use the extracted source ZIP and publish the site directory with an empty build command. For Netlify, the supplied netlify.toml publishes site. Host each theme at its project root or rewrite root-relative links for a shared catalog.

## Edit

Edit HTML, CSS and assets under site/. The photo inventory with Pexels source and license links is at site/assets/pexels/sources.json. Forms remain demonstrations.

Run npm run build to regenerate the portable document manifest and editable page JSON from the HTML. Run npm run check to test the exported adapter. The generated output is dist/.
