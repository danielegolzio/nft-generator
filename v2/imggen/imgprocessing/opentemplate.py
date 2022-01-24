from PIL import Image

def openTemplate():
    im = Image.open('imggen/imgprocessing/template.png')
    im = im.convert('RGB')

    return im