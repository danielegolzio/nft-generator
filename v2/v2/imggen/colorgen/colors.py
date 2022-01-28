import random
import numpy as np

def color_gen():
    """
    Generates the color of the body and background
    """
    # this makes the colors a little more varied
    prob = np.random.choice([True, False])
    if prob:
        BC = (np.random.randint(30, 210),np.random.randint(30, 210),np.random.randint(30, 210))
        BG = (255-BC[0],255-BC[1],255-BC[2])
    else:
        BG = (np.random.randint(30, 210),np.random.randint(30, 210),np.random.randint(30, 210))
        BC = (255-BG[0],255-BG[1],255-BG[2])
        
    return BC, BG