# Cloudflare Pages deployments

The workflow rebuilds the complete theme library from the newest versioned deployment ZIP per theme. Pushes to main that change a deployment ZIP, the build script, or the workflow trigger a run. You can also run it manually from Actions.

## One-time setup

1. Create a Cloudflare API token with Account > Cloudflare Pages > Edit on the account that owns the sitocal-themes Pages project.
2. In this repository's Settings > Secrets and variables > Actions, add repository secrets named CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID.
3. Run Deploy Sitocal themes to Cloudflare Pages from Actions. The first run deploys to the theme-library-preview branch. Open https://theme-library-preview.sitocal-themes.pages.dev/ and check the index, theme pages and images.
4. After validating the preview, add the repository variable CLOUDFLARE_PRODUCTION_ENABLED with value true, then run the workflow again. It will deploy to main and the production URL. Subsequent matching pushes will use the same destination.

Keep each deployable package under its theme folder using the existing <slug>-netlify-deploy-v<version>.zip naming convention. Publish packages from all theme updates to this repository so they are included in the workflow.
