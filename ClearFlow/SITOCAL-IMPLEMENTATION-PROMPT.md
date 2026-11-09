# Implementation prompt for the Sitocal repository

Copy the following brief into a coding session with the actual Sitocal source repository and the ClearFlow source ZIP available. Supply the published Netlify theme origin when available. A local extracted package is sufficient for development and automated tests.

---

You are working in the actual Sitocal website-builder codebase. Implement theme import, editing, persisted project builds, and user-controlled variations for the attached ClearFlow v1.2.0 package. Do the work, run appropriate tests, and report the changed files and remaining limitations. Do not stop at a plan. Do not assume that a Netlify URL or imported HTML automatically creates editable components.

## Objective and source material

The theme is a drain-cleaning/local-services mockup with 22 pages and three style/layout presets. Its forms, bookings and payment features must remain disconnected. Customers should choose the theme, create their own site, edit it, save it, create variations and build/export the result without modifying the original theme or another customer's project.

Inspect these actual package files first:

- dist/sitocal-theme.json: contract sitocal.portable-theme/1, version 1.2.0, pages, integrity inventory, editor and preset paths.
- dist/sitocal/pages/*.json: page documents and *.fields.json catalogs.
- dist/sitocal/editor.json: capabilities and limits.
- dist/sitocal/variations/presets.json: ClearFlow, Harbor Pro, Clearwater Local.
- sitocal-contract.mjs: reference validation, editing, section operations and renderer.
- render-project.mjs: offline build reference using saved project documents.
- README.md and test-sitocal.mjs: usage, constraints and tested behavior.

Treat this as a proposed external interchange contract, not Sitocal's existing schema. Do not dynamically import or execute downloaded JavaScript. Use the reference code only after reviewing and adapting it into the trusted codebase.

## 1. Inspect the repository and identify the real architecture

Read repository instructions and inspect the existing theme registry, saved-page format, editor component registry, project persistence, tenant authorization, asset storage, preview renderer, build/export pipeline and publishing integrations. Inspect at least one real existing theme and a representative saved page. Identify framework and validation libraries from the repository; reuse existing conventions.

Produce a concise mapping from actual file paths/modules to responsibilities. Locate how revisions, undo/redo, draft/published state and site-wide settings currently work. Do not invent folder names or introduce a second persistence system without need. Keep existing themes backward compatible. Add a feature gate if this is the repository's established rollout practice.

## 2. Implement the theme catalog and acquisition flow

Register a catalog entry with theme ID, package version, category, preview origin, manifest URL and a thumbnail generated from the actual preview. Do not present a generated illustration as a screenshot. Include “Preview” and “Use this theme” actions using the existing design system.

Support the local fixture for tests and a configured HTTPS manifest URL for normal imports. Read the manifest first; validate supported schema/version, required fields, route uniqueness and file inventory before creating a project. Fetch its listed page documents, field catalogs, presets and required assets. Derive all URLs using a URL parser and the approved package origin. Verify byte counts and hashes. The manifest itself must be trusted via the catalog/version policy; hashes supplied by an untrusted author are not authentication.

Use the server-side import service for acquisition if appropriate to the existing architecture. Apply SSRF controls: reject credentials, non-HTTPS public origins, loopback/private/link-local/metadata destinations and redirect escapes; validate resolved destinations as well as the initial hostname. Use explicit development-only fixtures for localhost tests. Bound redirects, timeouts, file count, individual bytes, total bytes, JSON depth and node count. Reject absolute/archive traversal paths, duplicate entries and unsupported content. Do not execute scripts or allow raw CSS/HTML insertion solely because a hash matches. Copy public assets without forwarding the user's authentication to the theme host.

Make import atomic and tenant-scoped. Use an idempotency key so retries/double-clicks do not create duplicate projects. Stage assets and documents, then commit them together. Roll back staged data on failure. A deliberate second “create site” operation must be able to create a separate copy. Record theme ID/version, manifest digest and source-node mapping as provenance; never persist secret credentials in the project.

## 3. Map the portable documents to native editable components

Prefer Sitocal's native schema. Provide a versioned adapter from the package to that schema and verify round-trip output. If native components cannot represent a section faithfully, implement a constrained portable-section component with typed editable fields; do not silently flatten the whole page into one uneditable HTML block or an iframe of the Netlify origin.

Map at least: page introduction/hero, assurance strip, service grid/cards, about section, process steps, service-area list, FAQ accordion, demo quote form, service detail, legal content, header/navigation and footer. Preserve section order, headings, semantic elements, accessible names, form labels, responsive behavior and the original SVG artwork. Data-section values are hints; use document node structure and IDs, not brittle text matching alone.

Allocate project-owned page, section, field and asset IDs. Preserve original ID mappings for provenance only. Rewrite navigation, asset paths and SVG/form/ARIA ID references correctly. Header/footer copies in the package should become native shared components where supported; avoid making “global brand edit” a collection of unrelated edits.

Services and locations are currently materialized pages/cards. Decide using the existing product model whether to keep them explicit or promote them into native collections with stable item IDs. If promoting them, document the mapping and test card-to-detail synchronization. Do not pretend the old theme.json arrays automatically synchronize all headings, cards and pages. The imported native documents/collections must become the sole source of truth.

## 4. Implement editor controls and save behavior

Expose text and heading edits, CTA labels and internal links, placeholders, accessible labels, page title/description, site-wide brand/navigation/footer settings, section order, section visibility, section duplication and design tokens. Use the repository's rich-text control only with its sanitization and supported marks; do not use arbitrary innerHTML for plain text fields.

Use supplied field catalogs as initial bindings. Recompute binding catalogs and section descriptors after duplicating or restructuring content. New sections need new IDs. Remap label-for attributes, ARIA references, fragment links and SVG IDs to avoid collisions. Keep decorative art separate from meaningful copy.

Integrate existing asset uploads for image-enabled native components. This theme contains SVG illustration, not an editable photographic image slot. If adding optional hero imagery, implement explicit image/alt-text fields with fallback illustration and tested responsive sizing; update the interchange adapter rather than injecting arbitrary URLs/markup.

Integrate undo/redo, autosave, draft revisions and existing conflict handling. Confirm that refreshing/reopening the editor restores all edits. Show clear pending/saved/error states. Never write customer edits to the remote template or regenerate customer pages from build.mjs, which only creates the original demo template.

## 5. Implement variations as independent draft states

Load the three package presets. Each contains an ID, name, layout (default/reversed/compact) and constrained CSS token values. Translate them to native theme settings. Applying a design preset must preserve user text, selected services, location data, links, uploaded assets, route structure and form configuration. Some decorative illustration/CSS colors remain fixed; do not claim complete recoloring without implementing it.

Offer “Create variation” by cloning a saved draft/revision. Give it a distinct ID and a readable name. Allow preview, switching, renaming, applying to the active draft and undoing the change using established product conventions. Editing variation B must not alter variation A. Only an explicit publish action may change the published site.

If Sitocal already has AI generation, add schema-constrained variation requests. Supply current content and allowed layout/token/component choices. Validate generated patches, reject unsupported components or executable content, preserve locked fields, and show a draft preview before applying. Do not require an AI API for the three deterministic presets or add a paid service without authorization. Do not invent reviews, certifications, service availability or business statistics.

## 6. Use saved project state for preview and builds

Render preview and final builds from the same saved native state. Keep the entire result independent of the original Netlify theme origin. Resolve copied assets to project-owned URLs and package local assets into exports. Do not embed a live remote template or hotlink its JavaScript.

Retain responsive mobile navigation, keyboard access, reduced-motion handling, FAQ interactions and demo-only form confirmation. The demo must not send network requests, create bookings or take payments. Review/bundle any needed runtime inside Sitocal, not via arbitrary remote module execution. Avoid deriving a real business's availability or claims from sample content.

Generate working routes for all 22 pages and a 404 response/page, with internal navigation intact. Preserve noindex for theme previews and customer drafts. Use existing publishing rules for customer sites; do not inadvertently carry demo legal copy or noindex into a purported production business launch without making those settings explicit. Respect the task's demo-only scope for this implementation.

Provide a complete export ZIP with generated pages, assets and hosting configuration. Deploy and source ZIPs have different purposes: deployment must not require the customer to reconstruct missing files. Use fresh build output to avoid obsolete routes. Continue using existing hosting integrations and authorization flows; do not replace them just to match this reference package.

## 7. Tests and acceptance criteria

Add meaningful tests in the repository's established stack. At minimum verify:

1. A valid fixture imports all 22 pages with assets, routes, editable fields and presets.
2. Unsupported version, malformed JSON/tree, bad hashes, oversized files, redirects to private hosts, traversal paths, executable attributes and failed fetches are rejected without partial projects.
3. Repeating the same import attempt is idempotent; intentional new imports are independent and cross-tenant access is denied.
4. Editing a homepage heading, CTA, metadata and a service detail persists after save/reload and appears identically in preview and exported HTML.
5. Updating a shared brand/footer affects the intended pages only. If native collections are added, a service update propagates to its cards and detail page without changing unrelated items.
6. Section reorder, hide and duplicate work; cloned form labels, SVG IDs and ARIA references are unique and correctly connected.
7. Applying each preset preserves user content. Creating/editing/switching variations preserves independent saved versions and leaves published state unchanged.
8. Exported routes and assets resolve without the Netlify theme origin being reachable. Test representative nested pages and 404 behavior.
9. Browser tests cover desktop and narrow mobile widths, keyboard navigation, menu open/close, FAQ expansion, demo validation and no form submission/network side effects.
10. Existing Sitocal themes continue to import/edit/build through their original flow.

Do not call the integration complete based only on a manifest download or iframe preview. Demonstrate the whole path: import → edit → save → reload → create variation → preview → build/export. If production publishing is outside the authorized scope, report that plainly and leave a tested build artifact ready.

## Deliverables

Implement the actual changes and provide:

- Exact source files changed and the reason for each group of changes.
- Any migration, seed/catalog entry, feature flag or environment setting required, with secret-free examples.
- A concise architecture note describing the interchange-to-native mapping and source of truth.
- Test results and a reviewable example export.
- Known unsupported fields/components and follow-up work, without claiming untested compatibility.

Proceed with routine implementation choices after inspection. Ask only for decisions that cannot be inferred and materially affect behavior or scope.

---

## Two follow-on variation prompts

1. **Harbor Pro:** Create a premium drain and sewer variation using the existing navy/copper preset and reversed desktop hero. Preserve all customer copy, routes and demo-only forms. Emphasize inspection and clear estimates, use compact process steps, and keep the mobile content order readable. Save it as a separate draft.
2. **Clearwater Local:** Create a friendly neighborhood plumbing variation using the existing blue preset and compact service cards. Preserve all business details and service-page links. Emphasize straightforward explanations and an easy mobile estimate journey. Keep forms disconnected and save it as a separate draft.
