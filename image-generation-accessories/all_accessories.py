from PIL import Image
dimensions = 400,400


cigarette = Image.open('accessories/cigarette.png')
cigarette = cigarette.resize(dimensions, resample=0)

christmas = Image.open("accessories/christmas.png")
christmas = christmas.resize(dimensions, resample=0)

gold_chain = Image.open("accessories/gold_chain.png")
gold_chain = gold_chain.resize(dimensions, resample=0)