import numpy as np
import random
from PIL import Image

################################################################################################################################################
# image data to list

def file_to_array(): # turns image_data file into a list
    file = open('image_data.txt', 'r')
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
    file.close()
    data = np.array(data)

    rarity(data)
    return data

################################################################################################################################################
# rarity generator

def rarity(data): # generates rarity for image
    number = random.randint(1, 1000)

    if number >= 1 and number <= 750: # 75% chance of getting this rarity
        rarity = 'common'
        common(data, rarity)
    
    # elif number >= 500 and number <= 750: # 25% chance of getting this rarity
    #     rarity = 'uncommon'
    #     uncommon()

    elif number >= 750 and number <= 850: # 10% chance of getting this rarity
        rarity = 'rare'
        rare(data, rarity)

    elif number >= 850 and number <= 900: # 5% chance of getting this rarity
        rarity = 'covert'
        covert(data, rarity)

    elif number >= 950 and number <= 960: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'red'
        legendary_r(data, rarity)

    elif number >= 960 and number <= 970: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'green'
        legendary_g(data, rarity)

    elif number >= 970 and number <= 980: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'blue'
        legendary_b(data, rarity)

    elif number == 999: # 0.1% chance of getting this rarity
        rarity = 'classified'
        main_colors = 'black'
        classified_blk(data, rarity)

    elif number == 1000: # 0.1% chance of getting this rarity
        rarity = 'classified'
        main_colors = 'white'
        classified_wht(data, rarity)

    return rarity

################################################################################################################################################
# color generator

def common(data, rarity):
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [255,255,255]
    EW = np.array(EW)
    EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
    EC = np.array(EC)
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    BC = np.array(BC)
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    OT = np.array(OT)
    BG = [250,249,213]
    BG = np.array(BG)
    BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

# def uncommon():
#     pass

def rare(data, rarity): # later on this will get complementary colors
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EW = np.array(EW)
    EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
    EC = np.array(EC)
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    BC = np.array(BC)
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    OT = np.array(OT)
    BG = [250,249,213]
    BG = np.array(BG)
    BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def covert(data, rarity):
    pass

def legendary_r(data, rarity):
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EW = np.array(EW)
    EC = [random.randint(50, 255),0,0]
    EC = np.array(EC)
    BC = [random.randint(50, 255),0,0]
    BC = np.array(BC)
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    OT = np.array(OT)
    BG = [250,249,213]
    BG = np.array(BG)
    BK = [random.randint(50, 255),0,0]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def legendary_b(data, rarity):
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EW = np.array(EW)
    EC = [0,random.randint(50, 255),0]
    EC = np.array(EC)
    BC = [0,random.randint(50, 255),0]
    BC = np.array(BC)
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    OT = np.array(OT)
    BG = [250,249,213]
    BG = np.array(BG)
    BK = [0,random.randint(50, 255),0]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def legendary_g(data, rarity):
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EW = np.array(EW)
    EC = [0,0,random.randint(50, 255)]
    EC = np.array(EC)
    BC = [0,0,random.randint(50, 255)]
    BC = np.array(BC)
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    OT = np.array(OT)
    BG = [250,249,213]
    BG = np.array(BG)
    BK = [0,0,random.randint(50, 255)]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def classified_blk(data, rarity):
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [255,255,255]
    EW = np.array(EW)
    ECr = random.randint(0, 150)
    EC = [ECr,ECr,ECr]
    EC = np.array(EC)
    BCr = random.randint(0, 150)
    BC = [BCr,BCr,BCr]
    BC = np.array(BC)
    OT = [255,255,255]
    OT = np.array(OT)
    BG = [250,249,213]
    BG = np.array(BG)
    BKr = random.randint(0,150)
    BK = [BKr,BKr,BKr]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def classified_wht(data, rarity):
    PF = [0,0,0] 
    PF = np.array(PF)
    EW = [255,255,255]
    EW = np.array(EW)
    ECr = random.randint(150, 255)
    EC = [ECr,ECr,ECr]
    EC = np.array(EC)
    BCr = random.randint(150, 255)
    BC = [BCr,BCr,BCr]
    BC = np.array(BC)
    OT = [255,255,255]
    OT = np.array(OT)
    BG = [28,28,28]
    BG = np.array(BG)
    BKr = random.randint(150,255)
    BK = [BKr,BKr,BKr]
    BK = np.array(BK)

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

################################################################################################################################################
# art generator

def art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK):
    for j in range(30):
        for k in range(30):
            if data[j][k] == 'PF':
                data[j][k].replace('PF',PF)
            elif data[j][k] == 'EW':
                data[j][k].replace('EW',EW)
            elif data[j][k] == 'EC':
                data[j][k].replace('EC',EC)
            elif data[j][k] == 'BC':
                data[j][k].replace('BC',BC)
            elif data[j][k] == 'OT':
                data[j][k].replace('OT',OT)
            elif data[j][k] == 'BG':
                data[j][k].replace('BG',BG)
            elif data[j][k] == 'BK':
                data[j][k].replace('BK',BK)
    
    print(data)


################################################################################################################################################

if __name__ == '__main__':
    file_to_array()
    