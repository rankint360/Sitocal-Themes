# Pestward

Pestward is a renamed clone of the NYC rodent-control reference at https://theme2preview.netlify.app/. It includes the homepage, service and location indexes, ten service pages, five borough pages, About and Contact.

The clone preserves the reference layout, colors and locally bundled artwork. It fixes two service URLs and replaces an unrelated testimonial logo with a quotation mark. Testimonial and business claims carried over from the reference are sample copy. Contact links route to the demo form, and the form sends and stores nothing.

## Deploy to Netlify

Extract the versioned deployment ZIP and upload the directory containing index.html. For a repository build, extract the source ZIP, set the build command to `npm run build` and publish `dist`. The supplied netlify.toml contains those settings.

## Edit and verify

Edit HTML in source/pages, assets in source/assets, and the brand in theme.json. Run `npm run build` and `npm run check` with Node.js. The site uses root-relative links and needs an HTTP server for local viewing. The build uses bundled files and requires no package installation.

source/capture.json records where the original assets came from. These static files can be adapted to a Sitocal import format.

Automated checks cover local links and assets, branding and demo form markup. Browser visual verification is pending.

## Variation prompts

1. Build an inspection-led version with a forest palette, a building perimeter diagram and a guide to common entry points.
2. Build a property-manager version with midnight blue, a maintenance schedule and a checklist for preparing a multi-unit building inspection.
