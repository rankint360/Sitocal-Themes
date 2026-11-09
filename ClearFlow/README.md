# ClearFlow — Sitocal portable theme 1.2.0

This is a complete static demo plus a proposed, implemented import contract. It is NOT already integrated with Sitocal's private source code. All forms remain demo-only. No external fonts, photos, trackers, bookings, or payment connections are required.

## Build and verify

Use a modern Node.js version supporting ES modules and structuredClone. No package installation is required.

```
npm run build
npm run check
npm run preview
```

Build creates 22 static pages, a 404 page, three homepage preset previews, and the editable package in dist/. Serve through HTTP; root-relative routes are not intended for file:// viewing.

Netlify: publish dist/, build command npm run build. For manual deployment, extract the deploy ZIP and upload its contents. The archive has index.html at its root. Netlify publishing has not been performed in this session.

## Import endpoints

- /sitocal-theme.json — versioned manifest, page/document/field references and SHA-256 file inventory
- /sitocal/pages/*.json — editable documents and field catalogs
- /sitocal/editor.json — controls, runtime contract, known limitations
- /sitocal/variations/presets.json — forest, navy/copper, and blue palettes/layouts
- /sitocal/reference-adapter.mjs — auditable reference code, NOT code to execute directly from a remote origin
- /variations/clearflow/, /variations/harbor-pro/, /variations/clearwater-local/ — homepage examples; links navigate to the base theme

Public static assets permit cross-origin GET through Netlify _headers. CORS does not authenticate a package. The receiving service must enforce URL, size, content and trust checks.

## Editable model

Contract identifier: sitocal.portable-theme/1. Each page has nodes (an HTML element/text tree), metadata bindings and section descriptors. Text edits target text-node IDs. Link/placeholder/accessible-label edits target element attributes. Rendered markup is escaped. SVG geometry is preserved as illustration, not exposed as arbitrary HTML editing.

Each field catalog lists nodeId, property, control and label. Title/description bindings are in document.metadata. Main children are reorderable, hideable and duplicable sections. IDs are stable for a given package version; Sitocal should allocate project-owned IDs at import and store original-ID mappings. Future template updates must not overwrite customer content.

Reference adapter exports validateDocument, findNode, visit, setText, setAttribute, setMetadata, sections, moveSection, setSectionVisible, duplicateSection, renderDocument. Duplicate IDs, form label references, ARIA ID references and SVG fragment references are remapped on section duplication. Recompute the fields and section catalogs after structural changes; exported catalogs describe the initial template only.

The renderer supports preset tokens and default/reversed/compact layouts. Variations are design settings applied to a copy of the same content, not new remote sites. Runtime must be a reviewed, locally bundled version of assets/app.js. The adapter is a reference implementation, not a complete hostile-package security boundary.

## Source of truth and project building

build.mjs produces the original template. export-sitocal.mjs converts this generator's controlled HTML into editable documents, then renders deployed HTML from those documents. The small tokenizer is deliberately scoped to this template; it is not an arbitrary HTML importer.

After a customer imports the theme, the customer's saved documents become the source of truth. Do NOT rerun build.mjs over customer content. Sitocal should render its native project representation, or use render-project.mjs as an offline reference. Prepare a separate project directory with project.json, pages/*.json and reviewed assets/:

```json
{
  "contract": "sitocal.portable-project/1",
  "pages": [{"path":"/","document":"pages/home.json"}],
  "preset": {"layout":"default","tokens":{"--green":"#173f35","--lime":"#d8ed8c"}}
}
```

```
node render-project.mjs PROJECT_DIRECTORY OUTPUT_DIRECTORY
```

Use a fresh output directory for each build to avoid obsolete pages. This reference builder keeps the demo/noindex behavior. Real customer launches require an explicit product decision about business content, indexing, legal content and service connections.

## Current limitations to implement in Sitocal

- No existing Sitocal API, database, component registry or authentication has been assumed.
- Header/footer instances are page-local. Promote them to native shared components for global editing.
- Service/location cards and detail pages are materialized content. Promote them to native collections if automatic cross-page synchronization is desired.
- The original SVG is bundled; there are no photographic image slots yet. Add image/upload controls via Sitocal's existing asset model rather than accepting arbitrary SVG code.
- Built-in palettes change tokens; some decorative colors in CSS/SVG remain fixed. They are presets, not total automatic recoloring.
- Reference validation is intentionally restrictive. Extend it deliberately alongside native component support.

See SITOCAL-IMPLEMENTATION-PROMPT.md for the complete implementation brief and acceptance tests.
