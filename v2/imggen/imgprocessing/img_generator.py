from PIL import Image
import numpy as np

def img_generator(BC, BG, im):
    """
    Generates the standard duck image with no accessories
    """
    new_img = im.copy()
    new_img[np.where((new_img==(255,0,0)).all(axis=2))] = BG
    new_img[np.where((new_img==(0,255,0)).all(axis=2))] = BC

    dimensions = (420,420)

    # array handling with numpy
    new_img = np.array(new_img, dtype=np.uint8)
    new_img = new_img.reshape(30,30,3)

    # using PIL to turn the RGB values into an image
    img_data = Image.fromarray(new_img, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)

    return img_data
