import numpy as np
import random
from PIL import Image

################################################################################################################################################
# image data to list

def file_to_array(): # turns image_data file into a list
    file = open('image_data.txt', 'r')
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
    file.close()

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
    EW = [255,255,255]
    EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

# def uncommon():
#     pass

def rare(data, rarity): # later on this will get complementary colors
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def covert(data, rarity):
    pass

def legendary_r(data, rarity):
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [random.randint(50, 255),0,0]
    BC = [random.randint(50, 255),0,0]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [random.randint(50, 255),0,0]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def legendary_b(data, rarity):
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [0,random.randint(50, 255),0]
    BC = [0,random.randint(50, 255),0]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [0,random.randint(50, 255),0]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def legendary_g(data, rarity):
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0] 
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [0,0,random.randint(50, 255)]
    BC = [0,0,random.randint(50, 255)]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [0,0,random.randint(50, 255)]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def classified_blk(data, rarity):
    PF = [0,0,0] 
    EW = [255,255,255]
    ECr = random.randint(0, 150)
    EC = [ECr,ECr,ECr]
    BCr = random.randint(0, 150)
    BC = [BCr,BCr,BCr]
    OT = [255,255,255]
    BG = [250,249,213]
    BKr = random.randint(0,150)
    BK = [BKr,BKr,BKr]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

def classified_wht(data, rarity):
    PF = [0,0,0] 
    EW = [255,255,255]
    ECr = random.randint(150, 255)
    EC = [ECr,ECr,ECr]
    BCr = random.randint(150, 255)
    BC = [BCr,BCr,BCr]
    OT = [255,255,255]
    BG = [28,28,28]
    BKr = random.randint(150,255)
    BK = [BKr,BKr,BKr]

    art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
    return PF, EW, EC, BC, OT, BG, BK

################################################################################################################################################
# art generator

def art_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK):
    RGB_data = []
    # for i in range(0,30):
    print(rarity)
    for j in range(30):
        for k in range(30):
            if data[j][k] == 'PF':
                RGB_data.append(PF)
            elif data[j][k] == 'EW':
                RGB_data.append(EW)
            elif data[j][k] == 'EC':
                RGB_data.append(EC)
            elif data[j][k] == 'BC':
                RGB_data.append(BC)
            elif data[j][k] == 'OT':
                RGB_data.append(OT)
            elif data[j][k] == 'BG':
                RGB_data.append(BG)
            elif data[j][k] == 'BK':
                RGB_data.append(BK)
    
    dimensions = 480, 480

    RGB_data = np.array(RGB_data)
    RGB_data = RGB_data.reshape(30,30,3)
    
    img_data = Image.fromarray(RGB_data, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)
    img_data.save('duck-test.png')
    img_data.show()


################################################################################################################################################

def main_loop(): # each image will be generated in this loop
    pass

if __name__ == '__main__':
    file_to_array()
    