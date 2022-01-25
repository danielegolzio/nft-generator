from PIL import Image
from imggen.accessorygen.accessories import *

"""
A file containing all of the accessories
"""
dimensions = 420,420

cigarette = Image.open("imggen/accessorygen/accessories/cigarette.png")
cigarette = cigarette.resize(dimensions, resample=0)

christmas = Image.open("imggen/accessorygen//accessories/christmas.png")
christmas = christmas.resize(dimensions, resample=0)

gold_chain = Image.open("imggen/accessorygen//accessories/gold_chain.png")
gold_chain = gold_chain.resize(dimensions, resample=0)

back_cap = Image.open("imggen/accessorygen//accessories/back_cap.png")
back_cap = back_cap.resize(dimensions, resample=0)

bow_tie = Image.open("imggen/accessorygen//accessories/bow_tie.png")
bow_tie = bow_tie.resize(dimensions, resample=0)

joint = Image.open("imggen/accessorygen//accessories/joint.png")
joint = joint.resize(dimensions, resample=0)

head_bandana_red = Image.open("imggen/accessorygen//accessories/head_bandana_red.png")
head_bandana_red = head_bandana_red.resize(dimensions, resample=0)

sunglasses = Image.open("imggen/accessorygen//accessories/sunglasses.png")
sunglasses = head_bandana_red.resize(dimensions, resample=0)

heart = Image.open("imggen/accessorygen//accessories/sunglasses.png")
heart = head_bandana_red.resize(dimensions, resample=0)

hats = [
    christmas,
    back_cap,
    heart
]
eyes = [
    head_bandana_red,
    sunglasses
]
mouth = [
    cigarette,
    joint
]
body = [
    gold_chain,
    bow_tie
]