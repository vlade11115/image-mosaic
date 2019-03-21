# Image Mosaic

Produce a mosaic from images.

## How to install dependencies

Assuming you have Python (and `pip`) at your disposal, install the dependencies like so:

```bash
pip install git+https://github.com/vlade11115/image-mosaic.git
```

## How to use the image mosaic script

This script is easy to use.

Once you have a good library of images to use as mosaic tiles, find an image that you would like to
turn into a mosaic and resize it to a small size using your favourite image editing tool. I suggest
keeping your input image to about 32x32 pixels if you can (because the mosaic will be 64x bigger).
Then run the mosaic script like so:

```bash
mosaic ./directory/containing/tiles ./path/to/input.jpg ./path/to/output.jpg
```

You should see a mosaic appear, called `output.jpg`.
