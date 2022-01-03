import numpy as np
import random
from PIL import Image, ImageOps
import os
import time
from all_accessories import *
from colors import *



# lists containing all accessories
hats = [christmas, back_cap]

mouth = [cigarette, joint]

eyes = [head_bandana_red]

body = [gold_chain, bow_tie]

funky = ['upsidedown']



# generates all the accessories that the duck will have
def accessory_gen():
    hat_item_bool = random.choice([True, False])
    mouth_item_bool = random.choice([True, False])
    eye_item_bool = random.choice([True, False])
    body_item_bool = random.choice([True, False])
    funky_item_bool = random.choice([True, False])
    
    if hat_item_bool:
        hat_item = random.choice(hats)
    else:
        hat_item = None
        
    if mouth_item_bool:
        mouth_item = random.choice(mouth)
    else:
        mouth_item = None
        
    if eye_item_bool:
        eye_item = random.choice(eyes)
    else:
        eye_item = None
        
    if body_item_bool:
        body_item = random.choice(body)
    else:
        body_item = None
        
    # if funky_item_bool:
    #     # funky_item = random.choice(funky)
    #     funky_item = None
    # else:
    #     funky_item = None
        
    return hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool



# generates base image based on generated colors
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
    dimensions = (400,400)

    # array handling with numpy
    RGB_data = np.array(RGB_data, dtype=np.uint8)
    RGB_data = RGB_data.reshape(30,30,3)
            
    # using PIL to turn the RGB values into an image
    img_data = Image.fromarray(RGB_data, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)

    return img_data



# layers all of the generated accessories onto the duck
def img_layering(i, img_data, PATH, hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool):
    if hat_item_bool:
        img_data.paste(hat_item, (0,0), hat_item)
        img_data.save(f'{PATH}/duck-{i+1}.png')
    if mouth_item_bool:
        img_data.paste(mouth_item, (0,0), mouth_item)
        img_data.save(f'{PATH}/duck-{i+1}.png')
    if body_item_bool:
        img_data.paste(body_item, (0,0), body_item)
        img_data.save(f'{PATH}/duck-{i+1}.png')
    if eye_item_bool:
        img_data.paste(eye_item, (0,0), eye_item)
        img_data.save(f'{PATH}/duck-{i+1}.png')



# turns the txt file contianing the image data into a list
def txt_img_file():
    # turns image_data file into a list
    file = open('image-data/image_data.txt', 'r')
    # new array that contains all RGB pixel values
    data = [line.strip('\n')[:-1].split(',') if line[-2] == ',' else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    return data



# gets the user to input how many images they want generated
def image_num():
    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input('How many images would you like to generate?: '))
            if loop_counter < 1: # User entered value less than 1
                print('Number of images must be at least 1.')
            else: # Value is an integer and greater than or equal to 1
                break
        except ValueError:
            print('Wrong input...')

    return loop_counter



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



# main loop which generates the requested number of images
def main_loop():

    PATH = makeNFTsDir()
    
    data = txt_img_file()

    loop_counter = image_num()
    
    # takes the starting time
    start_time = time.time()
    
    # main loop
    for i in range(0, loop_counter):
        # generates rarity
        PF, EW, EC, BC, OT, BG, BK = color_gen()

        img_data = img_generator(data, PF, EW, EC, BC, OT, BG, BK)

        hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool = accessory_gen()
        
        img_layering(i ,img_data, PATH, hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool)
        
    # prints elapsed time to generate images rounded to 2 decimal places
    print(f'Process finished --- {round(time.time()-start_time, 2)}s seconds ---')



if __name__ == '__main__':
    main_loop()