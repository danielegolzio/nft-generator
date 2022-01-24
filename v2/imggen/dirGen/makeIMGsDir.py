import os

# Creates directory to store generated images
def makeIMGsDir():
    cwd = os.getcwd()
    path = os.path.join(cwd, 'Images')

    # Try and make the image/ dir assuming it doesn't exist
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path