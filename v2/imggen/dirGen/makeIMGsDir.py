import os


def makeIMGsDir():
    """
    Creates the directory to store the images
    """
    cwd = os.getcwd()
    path = os.path.join(cwd, "Images")

    # Try and make the image/ dir assuming it doesn't exist
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path
