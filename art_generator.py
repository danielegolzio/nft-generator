import numpy as np
import random
from PIL import Image

################################################################################################################################################
# image data to list

def file_to_array(): # turns image_data file into a list
    file = open('image_data.txt', 'r')
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
    file.close()
    print(data)
    
    rarity(data)
    return data

################################################################################################################################################
# rarity generator

def rarity(data): # generates rarity for image
    number = random.randint(1, 1000)

    if number >= 1 and number <= 750: # 75% chance of getting this rarity
        rarity = 'common'
        common()
    
    # elif number >= 500 and number <= 750: # 25% chance of getting this rarity
    #     rarity = 'uncommon'
    #     uncommon()

    elif number >= 750 and number <= 850: # 10% chance of getting this rarity
        rarity = 'rare'
        rare()

    elif number >= 850 and number <= 900: # 5% chance of getting this rarity
        rarity = 'covert'
        covert()

    elif number >= 950 and number <= 960: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'red'
        legendary_r()

    elif number >= 960 and number <= 970: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'green'
        legendary_g()

    elif number >= 970 and number <= 980: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'blue'
        legendary_b()

    elif number == 999: # 0.1% chance of getting this rarity
        rarity = 'classified'
        main_colors = 'black'
        classified_blk()

    elif number == 1000: # 0.1% chance of getting this rarity
        rarity = 'classified'
        main_colors = 'white'
        classified_wht()

    art_generator(data, rarity)
    return rarity

################################################################################################################################################
# color generator

def common():
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

    return PF, EW, EC, BC, OT, BG, BK

# def uncommon():
#     pass

def rare():
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

    return PF, EW, EC, BC, OT, BG, BK

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

################################################################################################################################################
# art generator

def art_generator(data, rarity):
    for i in range(50): # main loop for generating art
        pass

################################################################################################################################################

if __name__ == '__main__':
    file_to_array()
    