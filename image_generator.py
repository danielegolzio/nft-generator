import numpy as np
import random
from PIL import Image, ImageOps
import os
import time
from color_generator import *



def txt_img_file():
    # turns image_data file into a list
    file = open('image-data/image_data.txt', 'r')
    # new array that contains all RGB pixel values
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    # turns christmas_image_data file into a list
    christmas_file = open('image-data/image_data_christmas.txt', 'r')
    # new array that contains all RGB pixel values
    christmas_data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in christmas_file.readlines()] # also made by Royce Chan
    christmas_file.close()

    return data, christmas_data


def image_num():
    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input('How many images would you like to generate?: '))
            if loop_counter < 1:  # User entered value less than 1
                print("Number of images must be at least 1.")
            else:  # Value is an integer and greater than or equal to 1
                break
        except ValueError:
            print('Wrong input...')

    return loop_counter


def rarity_gen():
    raritys = ['common', 'rare', 'legendary_r', 'legendary_g', 'legendary_b', 'classified_blk', 'classified_wht', 'christmas', 'upsidedown', 'smoking']
            
    # chooses rarity based on weight
    # choice = np.random.choice(raritys, 1, p=[0.50, 0.35, 0.04, 0.04, 0.04, 0.01, 0.01, 0.0075, 0.00125, 0.00125])
    choice = np.random.choice(raritys)
                 
    if choice == 'common':
        rarity = 'common'
        PF, EW, EC, BC, OT, BG, BK, CH = common()

    elif choice == 'rare':
        rarity = 'rare'
        PF, EW, EC, BC, OT, BG, BK, CH = rare()

    elif choice == 'legendary_r':
        rarity = 'legendary'
        main_colors = 'red'
        PF, EW, EC, BC, OT, BG, BK, CH = legendary_r()

    elif choice == 'legendary_g':
        rarity = 'legendary'
        main_colors = 'green'
        PF, EW, EC, BC, OT, BG, BK, CH = legendary_g()

    elif choice == 'legendary_b':
        rarity = 'legendary'
        main_colors = 'blue'
        PF, EW, EC, BC, OT, BG, BK, CH = legendary_b()

    elif choice == 'classified_blk':
        rarity = 'classified'
        PF, EW, EC, BC, OT, BG, BK, CH = classified_blk()

    elif choice == 'classified_wht':
        rarity = 'classified'
        PF, EW, EC, BC, OT, BG, BK, CH = classified_wht()

    # 0.1% chance of getting this rarity
    elif choice == 'christmas':
        rarity = 'christmas'
        PF, EW, EC, BC, OT, BG, BK, CH = christmas()

    # 0.01% chance of getting this rarity
    elif choice == 'upsidedown':
        rarity = 'upside down'
        PF, EW, EC, BC, OT, BG, BK, CH = upsidedown()
        
    elif choice == 'smoking':
        rarity = 'smoking'
        PF, EW, EC, BC, OT, BG, BK, CH = smoking()
    
    return PF, EW, EC, BC, OT, BG, BK, CH, rarity

def img_generator(i, christmas_data, data, PATH, rarity, PF, EW, EC, BC, OT, BG, BK, CH):
    RGB_data = []

    # makes a new array replacing the letters with the generated RGB colors
    if rarity == 'christmas':
        for j in range(30):
            for k in range(30):
                if christmas_data[j][k] == 'PF':
                    RGB_data.append(PF)
                elif christmas_data[j][k] == 'EW':
                    RGB_data.append(EW)
                elif christmas_data[j][k] == 'EC':
                    RGB_data.append(EC)
                elif christmas_data[j][k] == 'BC':
                    RGB_data.append(BC)
                elif christmas_data[j][k] == 'OT':
                    RGB_data.append(OT)
                elif christmas_data[j][k] == 'BG':
                    RGB_data.append(BG)
                elif christmas_data[j][k] == 'BK':
                    RGB_data.append(BK)
                elif christmas_data[j][k] == 'CH':
                    RGB_data.append(CH)
    else:
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

    # new dimensions for image
    dimensions = 480,480

    # array handling with numpy
    RGB_data = np.array(RGB_data, dtype=np.uint8)
    RGB_data = RGB_data.reshape(30,30,3)
            
    # using PIL to turn the RGB values into an image
    img_data = Image.fromarray(RGB_data, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)
    # img_data.show()

    # flips image if its upside down rarity
    if rarity == 'upside down':
        img_data = ImageOps.flip(img_data)
        img_data.save(f'{PATH}/duck-{i+1}.png')
    
    elif rarity == 'smoking':
        cigarette = Image.open("accessories/cigarette.png")
        cigarette = cigarette.resize(dimensions, resample=0)
        img_data.paste(cigarette, (0,0), cigarette)
        img_data.save(f'{PATH}/duck-{i+1}.png')
    
    else:
        img_data.save(f'{PATH}/duck-{i+1}.png')


# Creates directory to store generated images
def makeNFTsDir():
    cwd = os.getcwd()
    path = os.path.join(cwd, "Images")

    # Try and make the image/ dir assuming it doesn't exist
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path


def main_loop():
    # Make the NFT/ dir 
    PATH = makeNFTsDir()
    
    data, christmas_data = txt_img_file()

    loop_counter = image_num()
    
    # takes the starting time
    start_time = time.time()
    
    # main loop
    for i in range(0, loop_counter):
        # generates rarity
        PF, EW, EC, BC, OT, BG, BK, CH, rarity = rarity_gen()
        
        # generates image
        img_generator(i, christmas_data, data, PATH, rarity, PF, EW, EC, BC, OT, BG, BK, CH)

    # prints elapsed time to generate images rounded to 2 decimal places
    print(f"Process finished --- {round(time.time()-start_time, 2)}s seconds ---")


if __name__ == '__main__':
    main_loop()