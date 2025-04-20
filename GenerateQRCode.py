"""GenerateQRCode.py

Author: James Buntwal (James@Buntwal.com)

Description: 

    Creates a basic QR Code given a URL

    To run:

    >>> python GenerateQRCode.py 'target url' 'output/file/path.png'

"""

# Imports
import qrcode
import argparse
import pathlib


# Main Function
def main(   url : str,
            dest : pathlib.Path):
    """main
    
    This function generates a qr code that links to the given url.

    Args:
        url = URL to be converted to QR Code
        dest = Filepath to save output PNG

    Returns:
        None
    """

    # Raises an exception if the given file path is not a png
    force_PNG(path)

    # Instantiate QR Code object
    qr = qrcode.QRCode()

    # Add the URL
    qr.add_data(url)

    # Make the QR Code
    qr.make()

    # Generate the image
    img = qr.make_image()

    # Save the Image
    img.save(str(dest))


# 
def force_PNG(path : pathlib.Path):
    """force_PNG

    Raises an exception if the given file path is not a png.

    """
    if path.suffix.lower() != '.png':
        raise Exception("Output file path must include .png extension!")

    

if __name__ == "__main__":

    # Instantiate Argument parser
    ParserObject = argparse.ArgumentParser()
    
    # Add url and output path arguments to parser
    ParserObject.add_argument( 'url',
                                nargs = 1,
                                help = "URL to be converted to QR Code."
                                )
    ParserObject.add_argument( 'path',
                                nargs = 1,
                                help = "Output image file path. Must be a .png file."
                                )

    # Parse URL
    url = (ParserObject
        .parse_args()
        .url
        [0]
        )
    
    # Parse filepath and immediately convert str->pathlib.Path
    path = pathlib.Path(
        ParserObject
        .parse_args()
        .path
        [0]
        )

    # Run process
    main(url, path)
