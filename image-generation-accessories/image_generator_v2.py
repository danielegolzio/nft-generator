'''
This image generator will no longer include rarity's.
Instead the ducks have randomly added accessories. 
''' 
import numpy as np
import random
from PIL import Image, ImageOps
import os
import time



def txt_img_file():
    # turns image_data file into a list
    file = open('image-data/image_data.txt', 'r')
    # new array that contains all RGB pixel values
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    return data



def image_num():
    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input('How many images would you like to generate?: '))
            if loop_counter < 1: # User entered value less than 1
                print("Number of images must be at least 1.")
            else: # Value is an integer and greater than or equal to 1
                break
        except ValueError:
            print('Wrong input...')

    return loop_counter



def color_gen():
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0]
    EW = [50,50,50]
    EC = [random.randint(150, 255),random.randint(150, 255),random.randint(150, 255)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    BG = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [255-BG[0],255-BG[1],255-BG[2]]
    BK = [255-BC[0],255-BC[1],255-BC[2]]
    
    return PF, EW, EC, BC, OT, BG, BK



def img_generator(data, PF, EW, EC, BC, OT, BG, BK):
    RGB_data = []

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
    dimensions = (480,480)

    # array handling with numpy
    RGB_data = np.array(RGB_data, dtype=np.uint8)
    RGB_data = RGB_data.reshape(30,30,3)
            
    # using PIL to turn the RGB values into an image
    img_data = Image.fromarray(RGB_data, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)
    
    # generates the cigarette accessory
    cigarette = Image.open('accessories/cigarette.png')
    cigarette = cigarette.resize(dimensions, resample=0)
    
    return dimensions, img_data, cigarette



def accessory_gen():
    all_accessories =['cigarette', 'upsidedown']
    accessories_T_F = random.choice([True, False])
    
    if accessories_T_F == True:
        accessory = random.choices(all_accessories, weights=None, cum_weights=None, k=1)
        print(accessory)
    else:
        accessory = 'None'
        print(accessory)
    return accessory



def img_layering(i, cigarette, img_data, accessory, PATH):    
    if accessory[0] == 'cigarette':
        img_data.paste(cigarette, (0,0), cigarette)
        img_data.save(f'{PATH}/duck-{i+1}.png')
        
    elif accessory[0] == 'upsidedown':
        img_data = ImageOps.flip(img_data)
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
    
    data = txt_img_file()

    loop_counter = image_num()
    
    # takes the starting time
    start_time = time.time()
    
    # main loop
    for i in range(0, loop_counter):
        # generates rarity
        PF, EW, EC, BC, OT, BG, BK = color_gen()

        dimensions, img_data, cigarette = img_generator(data, PF, EW, EC, BC, OT, BG, BK)

        accessory = accessory_gen()
        
        img_layering(i, cigarette ,img_data, accessory, PATH)
        
    # prints elapsed time to generate images rounded to 2 decimal places
    print(f"Process finished --- {round(time.time()-start_time, 2)}s seconds ---")



if __name__ == '__main__':
    main_loop()