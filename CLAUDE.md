# Substack → Descript Social Video Pipeline

Automated pipeline that monitors the Fort Human Substack blog (descriptapp.substack.com) for new posts and creates Descript social video projects from each one.

## How it works

A scheduled remote routine runs daily and:

1. Fetches the RSS feed at `https://descriptapp.substack.com/feed`
2. Compares article URLs against `processed-articles.json` to find new posts
3. For each new post:
   - Downloads the hero image from the RSS `<enclosure>` element
   - Fetches the full article page and extracts text content
   - Creates a new Descript project via `import_media` (uploads hero image)
   - Runs `prompt_project_agent` with the article text + V4.0 social video prompt
   - On success: adds the article URL to `processed-articles.json` and commits
   - On failure (especially hero image download): DMs Sam on Slack and aborts

## Files

- `processed-articles.json` — Array of article URLs that have already been processed
- `prompt-v4.md` — The V4.0 Article → Social Video prompt template
- `CLAUDE.md` — This file

## Testing

To test with a specific article URL (bypassing RSS detection), the routine accepts a `test_url` parameter.

## Key details

- RSS feed URL: `https://descriptapp.substack.com/feed`
- Slack DM target: U060CHT8EMC (Sam)
- Descript project folder: "Substack Videos" (with team edit access)
- Hero image is in the RSS `<enclosure>` element (JPEG from Substack CDN)
