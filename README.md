# dissolve
Make an animated GIF that dissolves from one image to another using Python's Pillow.

## Summary
This example program shows the basic usage of the Python `argparse` module and the third-party [Pillow](https://python-pillow.org) library. In particular, modifying images at the pixel level and creating animated GIFs is demonstrated.

## Requirements
This program was tested on Python 3.7, and should work on newer versions. You must have the `Pillow` library installed. For example, `pip3 install pillow`. It was tested with Pillow 7.1.2.

## Running

```
python3 dissolve.py -h           
usage: dissolve [-h] source destination name

positional arguments:
  source       The image to dissolve from.
  destination  The image to dissolve to.
  name         The name for the animated GIF file.
```

## Example

```
python3 dissolve.py example1.jpeg example2.jpeg result.gif
```
![result.gif](result.gif)

## License
Licensed under the Apache License, version 2.0