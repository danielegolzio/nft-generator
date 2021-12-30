'''
This image generator will no longer include rarity's.
Instead the ducks have randomly added accessories. 
''' 
import numpy as np
import random
from PIL import Image, ImageOps
import os
import time



def main_loop():
    # Make the NFT/ dir
    PATH = makeNFTsDir()

    # array used to display rarities - can be seen in last procedure
    rarity_array = []

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

    # Start time for counting elapsed image generation time
    start_time = time.time()

    # turns image_data file into a list
    file = open('image_data.txt', 'r')

    # new array that contains all RGB pixel values
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    # turns christmas_image_data file into a list
    christmas_file = open('image_data_christmas.txt', 'r')

    # new array that contains all RGB pixel values
    christmas_data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in christmas_file.readlines()] # also made by Royce Chan
    christmas_file.close()

    # takes the starting time
    start_time = time.time()

    # main loop
    for counter in range(0, loop_counter):

        # rarity generator
        def accessory_gen():
            all_accessories = ['cigarette', 'upsidedown']
            accessories_T_F = random.choice([True, False])
            if accessories_T_F:
                num_of_accessories = random.randint(0, len(all_accessories))
                # accessories = np.random.choice(all_accessories, num_of_accessories)
                accessories = random.choices(all_accessories, weights=None, cum_weights=None, k=num_of_accessories)
                print(accessories)

                color(accessories, num_of_accessories)
                return accessories, num_of_accessories

            else:
                accessories = None
                num_of_accessories = None

                color(accessories, num_of_accessories)
                return accessories, num_of_accessories



        # color generator
        def color(accessories, num_of_accessories):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [0,0,0]
            EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [255-BC[0],255-BC[1],255-BC[2]]
            BG = [28,28,28]
            BK = [255-EC[0],255-EC[1],255-EC[2]]

            img_generator(num_of_accessories, accessories, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK



        # img generator
        def img_generator(num_of_accessories, accessories, PF, EW, EC, BC, OT, BG, BK):        
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
            dimensions = 480,480

            # array handling with numpy
            RGB_data = np.array(RGB_data, dtype=np.uint8)
            RGB_data = RGB_data.reshape(30,30,3)
            
            # using PIL to turn the RGB values into an image
            img_data = Image.fromarray(RGB_data, 'RGB')
            img_data = img_data.resize(dimensions, resample=0)

            # # flips image if its upside down rarity
            # if rarity == 'upside down':
            #     img_data = ImageOps.flip(img_data)
            
            # cigarette = Image.open("accessories/cigarette.png")
            # cigarette = cigarette.resize(dimensions, resample=0)
            # img_data.paste(cigarette, (0,0), cigarette)
            
            # img_data.save(f'{PATH}/duck-{i+1}.png')
            
            image_layering(img_data, accessories, dimensions, num_of_accessories)
            return img_data, accessories, dimensions, num_of_accessories
        
        
        def image_layering(img_data, accessories, dimensions, num_of_accessories):
            if accessories ==  None:
                return None

            else:
                for i in range(num_of_accessories):
                    if i == 'cigarette':
                        cigarette = Image.open("accessories/cigarette.png")
                        cigarette = cigarette.resize(dimensions, resample=0)
                        img_data.paste(cigarette, (0,0), cigarette)
                        img_data.save(f'{PATH}/duck-{counter+1}.png')
                        
                    elif i == 'upsidedown':
                        # flips image if its upside down rarity
                        img_data = ImageOps.flip(img_data)
                        img_data.save(f'{PATH}/duck-{counter+1}.png')
                    
        accessory_gen()

    accessory_gen()
    
    # Prints elapsed time to generate images rounded to 2 decimal places
    print(f"Process finished --- {round(time.time()-start_time, 2)}s seconds ---")



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



if __name__ == '__main__':
    main_loop()
    
