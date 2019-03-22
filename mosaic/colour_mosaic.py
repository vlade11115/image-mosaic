#! /usr/bin/env python
import glob
import os
import random
import sys
from operator import itemgetter

from PIL import Image

random.seed(42)
PIXEL_SIZE = 2 ** 6


def distance(a, b):
    dist = 0

    for left, right in zip(a, b):
        dist += left - right if left > right else right - left

    return dist


def average_colour(image, pixels):
    channels = len(pixels[0, 0])
    colours = [0] * channels
    for x in range(image.width):
        for y in range(image.height):
            for channel in range(channels):
                colours[channel] += pixels[x, y][channel]

    colours = [int(i / (image.width * image.height)) for i in colours]
    return colours


def generate_mosaic(tiles, image, out_path_or_file):
    for tile in tiles:
        tile['colour'] = average_colour(tile['image'], tile['pixels'])

    pixels = image.load()
    w, h = image.size

    output_dims = (w * PIXEL_SIZE, h * PIXEL_SIZE)
    output_image = Image.new("RGB", output_dims)

    pos_w = 0
    pos_h = 0

    for x in range(w):
        for y in range(h):
            for i in tiles:
                i["distance"] = distance(pixels[x, y], i["colour"])

            best_matches = sorted(tiles, key=itemgetter("distance"))
            choice = random.choice(best_matches[0:5])
            output_image.paste(choice["image"], (pos_w, pos_h))
            pos_h += PIXEL_SIZE

            if pos_h == output_dims[1]:
                pos_h = 0
                pos_w += PIXEL_SIZE

    output_image.save(out_path_or_file)


def tile_image(image):
    image = image.resize((PIXEL_SIZE, PIXEL_SIZE))
    pixels = image.load()
    return {
        "image": image,
        "pixels": pixels,
    }


def load_images(image_dir):
    images = []

    for name in glob.iglob(image_dir):
        path = os.path.join(image_dir, name)
        image = Image.open(path)

        images.append(tile_image(image))

    return images


def main():
    image_dir = os.path.join(sys.argv[1], '*.jpg')
    input_image = sys.argv[2]
    input_path = sys.argv[3]
    image = Image.open(input_image)

    generate_mosaic(load_images(image_dir), image, input_path)


if __name__ == "__main__":
    main()
