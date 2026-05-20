#!/usr/bin/env python3
"""
Fetch new Fort Human Substack articles via the Substack JSON API.

Compares against processed-articles.json and writes pending-articles.json
with full article data (title, subtitle, body text, hero image URL, date)
for any articles not yet processed.

Usage: python3 scripts/fetch_new_articles.py
  - Reads: processed-articles.json (from repo root)
  - Writes: pending-articles.json (to repo root)
  - Exit code 0: success (even if no new articles)
  - Exit code 1: fetch/parse error
"""

import json
import os
import re
import html
import sys
import urllib.request
import urllib.error

SUBSTACK_BASE = "https://descriptapp.substack.com"
ARCHIVE_URL = f"{SUBSTACK_BASE}/api/v1/archive?sort=new&limit=25"
POST_URL_TEMPLATE = f"{SUBSTACK_BASE}/api/v1/posts/{{slug}}"

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_FILE = os.path.join(REPO_ROOT, "processed-articles.json")
PENDING_FILE = os.path.join(REPO_ROOT, "pending-articles.json")


def fetch_json(url):
    """Fetch a URL and return parsed JSON."""
    req = urllib.request.Request(url, headers={"User-Agent": "SubstackToVideo/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def strip_html(body_html):
    """Convert HTML to plain text."""
    if not body_html:
        return ""
    h = body_html
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", h, flags=re.DOTALL)
    h = re.sub(r"<br\s*/?>", "\n", h)
    h = re.sub(
        r"</?(p|div|h[1-6]|blockquote|li|ul|ol|figure|figcaption|a|picture|source|img|tr|td|th|table|thead|tbody)[^>]*>",
        "\n",
        h,
    )
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h.strip()


def main():
    # Load already-processed URLs
    try:
        with open(PROCESSED_FILE) as f:
            processed = set(json.load(f))
    except FileNotFoundError:
        processed = set()

    # Fetch archive listing
    print(f"Fetching archive from {ARCHIVE_URL}")
    try:
        archive = fetch_json(ARCHIVE_URL)
    except Exception as e:
        print(f"ERROR: Failed to fetch archive: {e}", file=sys.stderr)
        sys.exit(1)

    # Find new articles
    new_posts = []
    for post in archive:
        url = post.get("canonical_url", "")
        if url and url not in processed:
            new_posts.append(post)

    print(f"Found {len(new_posts)} new article(s) out of {len(archive)} total")

    if not new_posts:
        # Write empty pending file
        with open(PENDING_FILE, "w") as f:
            json.dump([], f, indent=2)
        print("No new articles. pending-articles.json is empty.")
        return

    # Fetch full content for each new article
    pending = []
    for post in new_posts:
        slug = post.get("slug", "")
        title = post.get("title", "").strip()
        url = post.get("canonical_url", "")
        subtitle = post.get("subtitle", "").strip()
        cover_image = post.get("cover_image", "")
        post_date = post.get("post_date", "")

        # Parse date to YYYY-MM-DD
        date_str = post_date[:10] if post_date else ""

        print(f"  Fetching full content for: {title}")
        try:
            full_post = fetch_json(POST_URL_TEMPLATE.format(slug=slug))
            body_html = full_post.get("body_html", "") or ""
            body_text = strip_html(body_html)
        except Exception as e:
            print(f"  WARNING: Failed to fetch full post '{slug}': {e}", file=sys.stderr)
            body_text = ""

        article = {
            "title": title,
            "url": url,
            "slug": slug,
            "subtitle": subtitle,
            "date": date_str,
            "image_url": cover_image,
            "body_text": body_text,
            "body_length": len(body_text),
        }
        pending.append(article)
        print(f"    body: {len(body_text)} chars, image: {'YES' if cover_image else 'NO'}")

    # Write pending file
    with open(PENDING_FILE, "w") as f:
        json.dump(pending, f, indent=2)

    print(f"\nWrote {len(pending)} article(s) to pending-articles.json")


if __name__ == "__main__":
    main()
