import random


def color_gen():

    PF = [0,0,0]
    EW = [255,255,255]
    EC = [0,0,0]
    BC = [random.randint(70, 210),random.randint(70, 210),random.randint(70, 210)]
    BG = [255-BC[0],255-BC[1],255-BC[2]]
    OT = [50,50,50]
    BK = [255,198,110]
    
    return PF, EW, EC, BC, OT, BG, BK