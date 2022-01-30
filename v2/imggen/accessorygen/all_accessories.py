from PIL import Image
from imggen.accessorygen.accessories import *
from imggen.dimensions.dimensions import dimensions

"""
A file containing all of the accessories
"""

cigarette = Image.open("imggen/accessorygen/accessories/cigarette.png")
cigarette = cigarette.resize(dimensions, resample=0)

christmas = Image.open("imggen/accessorygen//accessories/christmas.png")
christmas = christmas.resize(dimensions, resample=0)

gold_chain = Image.open("imggen/accessorygen/accessories/gold_chain.png")
gold_chain = gold_chain.resize(dimensions, resample=0)

back_cap = Image.open("imggen/accessorygen/accessories/back_cap.png")
back_cap = back_cap.resize(dimensions, resample=0)

bow_tie = Image.open("imggen/accessorygen/accessories/bow_tie.png")
bow_tie = bow_tie.resize(dimensions, resample=0)

joint = Image.open("imggen/accessorygen/accessories/joint.png")
joint = joint.resize(dimensions, resample=0)

head_bandana_red = Image.open("imggen/accessorygen/accessories/head_bandana_red.png")
head_bandana_red = head_bandana_red.resize(dimensions, resample=0)

head_bandana_blue = Image.open("imggen/accessorygen/accessories/head_bandana_blue.png")
head_bandana_blue = head_bandana_blue.resize(dimensions, resample=0)

sunglasses = Image.open("imggen/accessorygen/accessories/sunglasses.png")
sunglasses = sunglasses.resize(dimensions, resample=0)

heart = Image.open("imggen/accessorygen/accessories/heart.png")
heart = heart.resize(dimensions, resample=0)

visor_red = Image.open("imggen/accessorygen/accessories/visor_red.png")
visor_red = visor_red.resize(dimensions, resample=0)

visor_blue = Image.open("imggen/accessorygen/accessories/visor_blue.png")
visor_blue = visor_blue.resize(dimensions, resample=0)

astronaut = Image.open("imggen/accessorygen/accessories/astronaut.png")
astronaut = astronaut.resize(dimensions, resample=0)

glasses = Image.open("imggen/accessorygen/accessories/glasses.png")
glasses = glasses.resize(dimensions, resample=0)

robo_eye = Image.open("imggen/accessorygen/accessories/robo_eye.png")
robo_eye = robo_eye.resize(dimensions, resample=0)

suit = Image.open("imggen/accessorygen/accessories/suit.png")
suit = suit.resize(dimensions, resample=0)

gucci_hoodie = Image.open("imggen/accessorygen/accessories/gucci_hoodie.png")
gucci_hoodie = gucci_hoodie.resize(dimensions, resample=0)

flame_tail = Image.open("imggen/accessorygen/accessories/flame_tail.png")
flame_tail = flame_tail.resize(dimensions, resample=0)

straw_hat = Image.open("imggen/accessorygen/accessories/straw_hat.png")
straw_hat = straw_hat.resize(dimensions, resample=0)

bikini = Image.open("imggen/accessorygen/accessories/bikini.png")
bikini = bikini.resize(dimensions, resample=0)

body_armour = Image.open("imggen/accessorygen/accessories/body_armour.png")
body_armour = body_armour.resize(dimensions, resample=0)

helmet = Image.open("imggen/accessorygen/accessories/helmet.png")
helmet = helmet.resize(dimensions, resample=0)

hats = [
    christmas,
    back_cap,
    heart,
    flame_tail,
    straw_hat,
    helmet
]
eyes = [
    head_bandana_red,
    head_bandana_blue,
    sunglasses,
    visor_red,
    visor_blue,
    astronaut,
    glasses,
    robo_eye,
    flame_tail
]
mouth = [
    cigarette,
    joint
]
body = [
    gold_chain,
    bow_tie,
    suit,
    gucci_hoodie,
    bikini,
    body_armour
]