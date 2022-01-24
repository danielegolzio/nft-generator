import random

def color_gen():
    PF = [0,0,0]
    EW = [255,255,255]
    EC = [0,0,0]
    
    # this makes the colors more varied
    prob = random.choice([True, False])
    if prob:
        BC = [random.randint(30, 220),random.randint(30, 220),random.randint(30, 220)]
        BG = [255-BC[0],255-BC[1],255-BC[2]]
    else:
        BG = [random.randint(30, 220),random.randint(30, 220),random.randint(30, 220)]
        BC = [255-BG[0],255-BG[1],255-BG[2]]
        
    OT = [50,50,50]
    BK = [255,198,110]
    
    return PF, EW, EC, BC, OT, BG, BK