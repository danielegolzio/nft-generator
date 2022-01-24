import random

def color_gen():
    """
    Generates the color of the body and background
    """
    # this makes the colors more varied
    prob = random.choice([True, False])
    if prob:
        BC = [random.randint(30, 210),random.randint(30, 210),random.randint(30, 210)]
        BG = [255-BC[0],255-BC[1],255-BC[2]]
    else:
        BG = [random.randint(30, 210),random.randint(30, 210),random.randint(30, 210)]
        BC = [255-BG[0],255-BG[1],255-BG[2]]
        
    return BC, BG