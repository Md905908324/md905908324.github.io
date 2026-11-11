# Hobbies gallery

Upload photos directly into this folder on GitHub and commit to `gh-pages`.
GitHub Pages automatically generates the photo list during deployment. **You do
not need to run a command or edit a JSON file.** Allow the normal Pages build to
finish, then reload the website.

Supported formats: JPG, JPEG, PNG, WebP, GIF, and AVIF. Subfolders are supported.
File names become captions: `Michigan-Stadium.jpg` becomes `Michigan Stadium`.

In Hobbies, click **Gallery unlock** and enter **myding**. With no photos, the
gallery displays a **Coming soon** placeholder. The password prompt is an
Easter egg only; this repository and its image files are public.

## How it works

`assets/gallery/index.json` is a Jekyll/Liquid template. GitHub Pages fills it
from `site.static_files` on each build. Keep Jekyll enabled (do not add a
`.nojekyll` file). No API keys, GitHub API requests, or additional workflows are
needed.

## Optional local preview

For a plain Python or other static file server, the frontend falls back to
`photos.json` because those servers do not process Liquid. If you want to
preview newly added photos locally, run:

```sh
python3 scripts/update-gallery.py
```

That command is only for local preview. Uploading through GitHub requires no
manual indexing step.
