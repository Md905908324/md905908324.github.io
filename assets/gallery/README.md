# Hobbies gallery

Add your photos here. Supported formats: JPG, JPEG, PNG, WebP, GIF, and AVIF.
Subfolders are supported. Hidden files and symbolic links are ignored.

Refresh the photo index from the repository root:

```sh
python3 scripts/update-gallery.py
```

Commit and push the images and generated `assets/gallery/photos.json` together.
Open **Off the clock** at the bottom of Hobbies to reveal the gallery.

File names become photo captions and alt text. For example,
`Michigan-Stadium.jpg` displays as `Michigan Stadium`. Edit the generated `alt`
text in `photos.json` for a more descriptive caption if desired; regenerating the
index restores captions from file names.

Only add photos you want publicly visible: this is a public website and
repository. The Easter egg hides the gallery in the interface, not the files.

No photos are included yet. The website displays an empty state until you add
images and refresh the index. The gallery requires no API keys or external photo
service.
