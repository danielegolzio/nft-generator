# generates the colors depending on the rarity
# then it turns the python list into a numpy array

import random as r
import numpy

def common():
    eyeWhiteColors = [255,0]
    eyeWhite = r.choice(eyeWhiteColors)
    PF = [0,0,0] 
    PF = numpy.array(PF)
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EW = numpy.array(EW)
    EC = [r.randint(0, 250),r.randint(0, 250),r.randint(0, 250)]
    EC = numpy.array(EC)
    BC = [r.randint(0, 255),r.randint(0, 255),r.randint(0, 255)]
    BC = numpy.array(BC)
    OT = [r.randint(100, 250),r.randint(100, 250),r.randint(100, 250)]
    OT = numpy.array(OT)
    BG = [250,249,213]
    BG = numpy.array(BG)
    BK = [r.randint(0, 255),r.randint(0, 255),r.randint(0, 255)]
    BK = numpy.array(BK)
    print(PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def uncommon():
    pass

def rare():
    pass

def covert():
    pass

def legendary_r():
    pass

def legendary_b():
    pass

def legendary_g():
    pass

def classified_blk():
    pass

def classified_wht():
    pass

if __name__ == '__main__':
    common()