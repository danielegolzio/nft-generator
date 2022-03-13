from PIL import Image
import cv2


def openTemplate():
    im = cv2.imread("imggen/imgprocessing/template.png")
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    return im
