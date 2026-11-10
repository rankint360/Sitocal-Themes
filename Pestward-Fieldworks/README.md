# Pestward Fieldworks

Pestward Fieldworks is a companion NYC rodent-control theme. Its forest, parchment and ochre palette frames an inspection-first homepage with an original building schematic and an expandable entry-point guide. It retains all 20 routes from Pestward.

## Deploy to Netlify

Extract the versioned deployment ZIP and upload the directory containing index.html. For a repository build, extract the source ZIP, set the build command to `npm run build` and publish `dist`. The supplied netlify.toml contains those settings.

## Edit and verify

Edit the inspection homepage sections in fieldworks-home.html, design tokens and layout in fieldworks.css, and shared page markup in source/pages. Run `npm run build` and `npm run check` with Node.js. The build uses bundled assets and requires no package installation.

Forms are demonstrations and send or store no information. Source business and service claims are illustrative. source/capture.json records the original asset URLs. This static package can be adapted to a Sitocal import format.

Automated checks cover local links and assets, branding, demo form markup and the inspection guide. Browser visual verification is pending.

## Variation prompts

1. Create a townhouse edition with a narrow-lot building diagram, brownstone details and a resident preparation checklist.
2. Create a commercial edition with a receiving-area inspection sketch, service-entry checklist and recurring maintenance scope.
