"""Assemble the production theme library from versioned deployment ZIPs."""

import argparse
import html
from html.parser import HTMLParser
import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

RELEASE = re.compile(r"([a-z0-9]+(?:-[a-z0-9]+)*)-netlify-deploy-v(\d+(?:\.\d+)+)\.zip")
ATTRIBUTE_PATH = re.compile(r"""(\b(?:href|src|action|poster|data-src|content)\s*=\s*['"])/(?!/)""", re.I)
CSS_PATH = re.compile(r"""(url\(\s*['"]?)/(?!/)""", re.I)
STATIC_LINK = re.compile(r"""\b(?:href|src|poster)\s*=\s*['"](/(?!/)[^'"]*)""", re.I)


def latest_releases(repo):
    releases = {}
    for path in sorted(repo.glob("*/*-netlify-deploy-v*.zip")):
        match = RELEASE.fullmatch(path.name)
        if not match:
            raise ValueError(f"Unrecognized deployment archive: {path}")
        slug, version = match.groups()
        parts = tuple(int(part) for part in version.split("."))
        key = parts + (0,) * max(0, 3 - len(parts))
        previous = releases.get(slug)
        if previous and (key == previous[0] or path.parent != previous[1].parent):
            raise ValueError(f"Ambiguous release for {slug}: {path}")
        if previous is None or key > previous[0]:
            releases[slug] = (key, path)
    return releases


def unpack_theme(archive, slug, output):
    destination = output / slug
    destination.mkdir()
    seen = set()
    with ZipFile(archive) as package:
        for entry in package.infolist():
            path = PurePosixPath(entry.filename)
            if path.is_absolute() or ".." in path.parts or "\\" in entry.filename or ":" in entry.filename:
                raise ValueError(f"Unsafe path in {archive}: {entry.filename}")
            if entry.is_dir() or path.name in {"_headers", "_redirects", "robots.txt", "theme.json", "sitocal-theme.json"} or "sitocal" in path.parts:
                continue
            target = destination.joinpath(*path.parts)
            if target in seen:
                raise ValueError(f"Duplicate path in {archive}: {path}")
            seen.add(target)
            if entry.file_size > 25 * 1024 * 1024:
                raise ValueError(f"Asset exceeds the Pages size limit: {path}")
            target.parent.mkdir(parents=True, exist_ok=True)
            data = package.read(entry)
            if path.suffix.lower() in {".html", ".css"}:
                content = CSS_PATH.sub(rf"\g<1>/{slug}/", data.decode("utf-8-sig"))
                if path.suffix.lower() == ".html":
                    content = ATTRIBUTE_PATH.sub(rf"\g<1>/{slug}/", content)
                data = content.encode("utf-8")
            target.write_bytes(data)
    if not (destination / "index.html").is_file():
        raise ValueError(f"Missing homepage for {slug}")


def validate_assets(output):
    missing = set()
    for file in output.rglob("*.html"):
        for value in STATIC_LINK.findall(file.read_text(encoding="utf-8")):
            path = unquote(urlsplit(html.unescape(value)).path).lstrip("/")
            target = output / path
            if not any(item.is_file() for item in (target, target / "index.html", output / (path + ".html"))):
                missing.add(value)
    if missing:
        raise ValueError("Missing paths: " + ", ".join(sorted(missing)[:25]))
    count = sum(path.is_file() for path in output.rglob("*"))
    if count > 20_000:
        raise ValueError(f"{count} files exceed the configured Pages deployment limit")
    return count


class ThemePhotos(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attributes):
        if tag == "img":
            src = dict(attributes).get("src") or ""
            if "/assets/pexels/" in src:
                self.paths.append(src)


def theme_card(slug, archive, output):
    name = slug.replace("-", " ").title()
    category = ""
    with ZipFile(archive) as package:
        metadata_path = next((entry for entry in package.namelist()
                              if PurePosixPath(entry) == PurePosixPath("theme.json")), None)
        if metadata_path:
            metadata = json.loads(package.read(metadata_path))
            name = metadata.get("name") or name
            category = metadata.get("category") or ""
    parser = ThemePhotos()
    parser.feed((output / slug / "index.html").read_text(encoding="utf-8"))
    photo = next((path for path in parser.paths if path.startswith(f"/{slug}/")
                  and (output / unquote(urlsplit(path).path).lstrip("/")).is_file()), "")
    image = f'<img src="{html.escape(photo)}" alt="" loading="lazy" decoding="async">' if photo else ""
    label = f'<span class="category">{html.escape(category)}</span>' if category else ""
    return (f'<li class="card" data-preview="/{slug}/"><div class="image">{image}'
            '<div class="preview-window"></div><span class="section-number" hidden>01</span></div>'
            f'<div class="details"><div>{label}<span class="section-name" hidden></span>'
            f'<h2>{html.escape(name)}</h2></div></div><div class="actions">'
            '<button type="button" data-full>Full screen</button>'
            f'<a href="/{slug}/" target="_blank" rel="noopener">Live demo</a>'
            f'<a class="select" href="https://app.sitocal.com/create-website?theme={slug}">Select</a>'
            '</div></li>')


def build(repo, output, minimum):
    releases = latest_releases(repo)
    if len(releases) < minimum:
        raise ValueError(f"Found {len(releases)} themes, expected at least {minimum}")
    output.mkdir(parents=True)
    for slug, (_, archive) in sorted(releases.items()):
        unpack_theme(archive, slug, output)
    cards = "\n".join(theme_card(slug, archive, output)
                      for slug, (_, archive) in sorted(releases.items()))
    template = Path(__file__).resolve().parents[1] / "pages" / "index.html"
    index = template.read_text(encoding="utf-8-sig").replace("<!-- THEME_CARDS -->", cards)
    (output / "index.html").write_text(index, encoding="utf-8")
    (output / "theme-preview.js").write_bytes(template.with_name("theme-preview.js").read_bytes())
    (output / "_headers").write_text(
        "/*\n  X-Robots-Tag: noindex, nofollow\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n", encoding="utf-8")
    (output / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    print(f"Validated {len(releases)} themes and {validate_assets(output)} files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--minimum-themes", type=int, default=29)
    args = parser.parse_args()
    build(args.repo, args.output, args.minimum_themes)
