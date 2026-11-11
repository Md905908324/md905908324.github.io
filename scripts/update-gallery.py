#!/usr/bin/env python3
"""Index gallery images for static hosting: python3 scripts/update-gallery.py."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote

SUPPORTED = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif'}


def create_index(directory, url_prefix):
    photos = []
    for image in sorted(directory.rglob('*'), key=lambda p: p.relative_to(directory).as_posix().casefold()):
        relative = image.relative_to(directory)
        if any(part.startswith('.') for part in relative.parts):
            continue
        if image.is_symlink() or not image.is_file() or image.suffix.lower() not in SUPPORTED:
            continue
        caption = re.sub(r'[-_]+', ' ', image.stem).strip() or 'Gallery photo'
        photos.append({'src': url_prefix.rstrip('/') + '/' + quote(relative.as_posix()), 'alt': caption})
    return photos


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parents[1] / 'assets' / 'gallery')
    parser.add_argument('--url-prefix', default='assets/gallery')
    args = parser.parse_args()
    directory = args.directory.resolve()
    if not directory.is_dir():
        parser.error(f'Gallery directory does not exist: {directory}')
    photos = create_index(directory, args.url_prefix)
    output = directory / 'photos.json'
    content = json.dumps(photos, ensure_ascii=False, indent=2) + '\n'
    if not output.exists() or output.read_text(encoding='utf-8') != content:
        output.write_text(content, encoding='utf-8')
    print(f'Indexed {len(photos)} photos in {output}')


if __name__ == '__main__':
    main()
