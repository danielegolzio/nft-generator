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
    data = [line.strip('\n')[:-1].split(',') if line[-2] == ',' else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    return data


def image_num():
    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input('How many images would you like to generate?: '))
            if loop_counter < 1:  # User entered value less than 1
                print('Number of images must be at least 1.')
            else:  # Value is an integer and greater than or equal to 1
                break
        except ValueError:
            print('Wrong input...')

    return loop_counter


def rarity_gen():
    raritys = ['common', 'rare', 'legendary_r', 'legendary_g', 'legendary_b', 'classified_blk', 'classified_wht', 'christmas', 'upsidedown']
            
    # chooses 1 rarity based on probability(p)
    choice = np.random.choice(raritys, 1, p=[0.50, 0.35, 0.04, 0.04, 0.04, 0.01, 0.01, 0.0075, 0.0025])
    #choice = random.choice(raritys)
         
    if choice == 'common':
        rarity = 'common'
        PF, EW, EC, BC, OT, BG, BK = common()

    elif choice == 'rare':
        rarity = 'rare'
        PF, EW, EC, BC, OT, BG, BK = rare()

    elif choice == 'legendary_r':
        rarity = 'legendary'
        main_colors = 'red'
        PF, EW, EC, BC, OT, BG, BK = legendary_r()

    elif choice == 'legendary_g':
        rarity = 'legendary'
        main_colors = 'green'
        PF, EW, EC, BC, OT, BG, BK = legendary_g()

    elif choice == 'legendary_b':
        rarity = 'legendary'
        main_colors = 'blue'
        PF, EW, EC, BC, OT, BG, BK = legendary_b()

    elif choice == 'classified_blk':
        rarity = 'classified'
        PF, EW, EC, BC, OT, BG, BK = classified_blk()

    elif choice == 'classified_wht':
        rarity = 'classified'
        PF, EW, EC, BC, OT, BG, BK = classified_wht()

    elif choice == 'christmas':
        rarity = 'christmas'
        PF, EW, EC, BC, OT, BG, BK = christmas()

    elif choice == 'upsidedown':
        rarity = 'upside down'
        PF, EW, EC, BC, OT, BG, BK = upsidedown()
        


def img_generator(i, data, PATH, rarity, PF, EW, EC, BC, OT, BG, BK):
    RGB_data = []

    # makes a new array replacing the letters with the generated RGB colors
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
    dimensions = (420,420)

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
    
    elif rarity == 'christmas':
        christmas = Image.open('accessories/christmas.png')
        christmas = christmas.resize(dimensions, resample=0)
        img_data.paste(christmas, (0,0), christmas)
        img_data.save(f'{PATH}/duck-{i+1}.png')
    
    else:
        img_data.save(f'{PATH}/duck-{i+1}.png')


# Creates directory to store generated images
def makeNFTsDir():
    cwd = os.getcwd()
    path = os.path.join(cwd, 'Images')

    # Try and make the image/ dir assuming it doesn't exist
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path


def main_loop():
    # Make the NFT/ dir 
    PATH = makeNFTsDir()
    
    data = txt_img_file()

    loop_counter = image_num()
    
    # takes the starting time
    start_time = time.time()
    
    # main loop
    for i in range(0, loop_counter):
        # generates rarity
        PF, EW, EC, BC, OT, BG, BK, rarity = rarity_gen()
        
        # generates image
        img_generator(i, data, PATH, rarity, PF, EW, EC, BC, OT, BG, BK)

    # prints elapsed time to generate images rounded to 2 decimal places
    print(f'Process finished --- {round(time.time()-start_time, 2)}s seconds ---')


if __name__ == '__main__':
    main_loop()