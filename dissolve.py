from PIL import Image
from argparse import ArgumentParser
from random import shuffle
from typing import List, Tuple

# the number of pixels to transfer each frame
TRANSFER_COUNT = 2500


def generate_pixels(width: int, height: int) -> List[Tuple[int, int]]:
    """Generate a list of all (x, y) pixel locations in random order"""
    pixels = []
    for w in range(width):
        for h in range(height):
            pixels.append((w, h))
    shuffle(pixels)
    return pixels


def transfer_pixels(source_img: Image, dest_img: Image, num_pixels: int, unused: List[Tuple[int, int]]):
    """Transfer *num_pixels* pixels from one image to another using *unused* pixel locations"""
    todo = num_pixels
    # unused is "false" if it is empty
    while todo > 0 and unused:
        pixel_loc = unused.pop()
        source_img.putpixel(pixel_loc, dest_img.getpixel(pixel_loc))
        todo -= 1


def create_dissolve(source: str, destination: str, name: str):
    """Create an animated gif named *name* dissolving from *source* to *destination*"""
    images = []
    try:
        with Image.open(source) as source_img, Image.open(destination) as dest_img:
            # if the second image is not the same size as the first image,
            # then resize it
            if source_img.size != dest_img.size:
                dest_img = dest_img.resize(source_img.size)
            # * is the unpack operator, so we are passing width, height form tuple
            unused_pixels = generate_pixels(*source_img.size)
            # add start image
            images.append(source_img.copy())
            # add transitional images
            while len(unused_pixels) > 0:
                transfer_pixels(source_img, dest_img, TRANSFER_COUNT, unused_pixels)
                images.append(source_img.copy())
            # add images back in the other direction
            for image in images[::-1]:
                images.append(image.copy())
            # write to disk
            images[0].save(name, save_all=True, append_images=images[1:],
                           duration=100, loop=0)
    except IOError:
        print("Cannot read source or destination as image.")


if __name__ == "__main__":
    # Parse the arguments
    file_parser = ArgumentParser("dissolve")
    file_parser.add_argument("source", help="The image to dissolve from.")
    file_parser.add_argument("destination", help="The image to dissolve to.")
    file_parser.add_argument("name", help="The name for the animated GIF file.")
    arguments = file_parser.parse_args()
    create_dissolve(arguments.source, arguments.destination, arguments.name)
