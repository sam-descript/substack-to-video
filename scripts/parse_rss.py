#!/usr/bin/env python3
"""Parse the Fort Human Substack RSS feed and output structured JSON for each article."""

import sys
import json
import re
import html
import xml.etree.ElementTree as ET
from datetime import datetime

FEED_URL = "https://descriptapp.substack.com/feed"
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}


def parse_pubdate(pubdate_str):
    """Convert RSS pubDate to YYYY-MM-DD."""
    try:
        dt = datetime.strptime(pubdate_str, "%a, %d %b %Y %H:%M:%S %Z")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return pubdate_str


def extract_body_text(content_encoded):
    """Strip HTML from content:encoded to get plain article text."""
    if not content_encoded:
        return ""
    h = content_encoded
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
    xml_text = sys.stdin.read()
    root = ET.fromstring(xml_text)

    articles = []
    for item in root.findall(".//item"):
        title_el = item.find("title")
        link_el = item.find("link")
        desc_el = item.find("description")
        pubdate_el = item.find("pubDate")
        enclosure_el = item.find("enclosure")
        content_el = item.find("content:encoded", NS)

        title = title_el.text.strip() if title_el is not None and title_el.text else ""
        link = link_el.text.strip() if link_el is not None and link_el.text else ""
        subtitle = desc_el.text.strip() if desc_el is not None and desc_el.text else ""
        pubdate = pubdate_el.text.strip() if pubdate_el is not None and pubdate_el.text else ""
        image_url = enclosure_el.get("url", "") if enclosure_el is not None else ""
        body_text = extract_body_text(content_el.text if content_el is not None else "")

        articles.append({
            "title": title,
            "url": link,
            "subtitle": subtitle,
            "date": parse_pubdate(pubdate),
            "image_url": image_url,
            "body_text": body_text,
            "body_length": len(body_text),
        })

    json.dump(articles, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
