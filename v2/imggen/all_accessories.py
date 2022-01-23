from PIL import Image
from imggen.accessories import *

dimensions = 420,420

cigarette = Image.open("imggen/accessories/cigarette.png")
cigarette = cigarette.resize(dimensions, resample=0)

christmas = Image.open("imggen/accessories/christmas.png")
christmas = christmas.resize(dimensions, resample=0)

gold_chain = Image.open("imggen/accessories/gold_chain.png")
gold_chain = gold_chain.resize(dimensions, resample=0)

back_cap = Image.open("imggen/accessories/back_cap.png")
back_cap = back_cap.resize(dimensions, resample=0)

bow_tie = Image.open("imggen/accessories/bow_tie.png")
bow_tie = bow_tie.resize(dimensions, resample=0)

joint = Image.open("imggen/accessories/joint.png")
joint = joint.resize(dimensions, resample=0)

head_bandana_red = Image.open("imggen/accessories/head_bandana_red.png")
head_bandana_red = head_bandana_red.resize(dimensions, resample=0)