import numpy as np
import random
from PIL import Image
import os



def main_loop():
    # Make the NFT/ dir 
    PATH = makeNFTsDir()

    # array used to display rarities - can be seen in last procedure
    rarity_array = []

    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input('How many images would you like to generate?: '))
            break
        except ValueError:
            print('wrong input...')

    # turns image_data file into a list
    file = open('image_data.txt', 'r')
    # new array that contains all RGB pixel values
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    # main loop
    for i in range(0, loop_counter):
        
        # rarity generator
        def rarity(data):
            number = random.randint(1, 1000)
            
            # 50% chance of getting this rarity
            if number >= 1 and number <= 500:
                rarity = 'common'
                common(data, rarity)
                return rarity
            
            # 25% chance of getting this rarity
            elif number >= 500 and number <= 750:
                rarity = 'uncommon'
                uncommon(data, rarity)
                return rarity

            # 10% chance of getting this rarity
            elif number >= 750 and number <= 850:
                rarity = 'rare'
                rare(data, rarity)
                return rarity

            # 5% chance of getting this rarity
            elif number >= 850 and number <= 900:
                rarity = 'covert'
                covert(data, rarity)
                return rarity

            # 1% chance of getting this rarity
            elif number >= 950 and number <= 960:
                rarity = 'legendary'
                main_colors = 'red'
                legendary_r(data, rarity)
                return rarity

            # 1% chance of getting this rarity
            elif number >= 960 and number <= 970:
                rarity = 'legendary'
                main_colors = 'green'
                legendary_g(data, rarity)
                return rarity

            # 1% chance of getting this rarity
            elif number >= 970 and number <= 980:
                rarity = 'legendary'
                main_colors = 'blue'
                legendary_b(data, rarity)
                return rarity

            # 0.1% chance of getting this rarity
            elif number == 999:
                rarity = 'classified'
                main_colors = 'black'
                classified_blk(data, rarity)
                return rarity

            # 0.1% chance of getting this rarity
            elif number == 1000:
                rarity = 'classified'
                main_colors = 'white'
                classified_wht(data, rarity)
                return rarity
            


        # color generator for common rarity
        def common(data, rarity):
            PF = [0,0,0]
            EW = [255,255,255]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK
        
        # color generator for uncommon rarity
        def uncommon(data, rarity):
            PF = [0,0,0]
            EW = [0,0,0]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK
        
        # color generator for rare rarity
        def rare(data, rarity): # later on this will get complementary colors...
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        # color generator for covert rarity
        def covert(data, rarity): # still need to decide how the colors will look here...
            pass

        # color generator for legendary rarity
        def legendary_r(data, rarity):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [random.randint(50, 255),0,0]
            BC = [random.randint(50, 255),0,0]
            OT = [random.randint(100, 250),0,0]
            BG = [random.randint(1, 255),0,0]
            BK = [random.randint(50, 255),0,0]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK
        
        # color generator for legendary rarity
        def legendary_g(data, rarity):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [0,random.randint(50, 255),0]
            BC = [0,random.randint(50, 255),0]
            OT = [0,random.randint(100, 255),0]
            BG = [0,random.randint(1, 255),0]
            BK = [0,random.randint(50, 255),0]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK
        
        # color generator for legendary rarity
        def legendary_b(data, rarity):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [0,0,random.randint(50, 255)]
            BC = [0,0,random.randint(50, 255)]
            OT = [0,0,random.randint(100, 250)]
            BG = [0,0,random.randint(1, 255)]
            BK = [0,0,random.randint(50, 255)]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK

        # color generator for classified rarity
        def classified_blk(data, rarity):
            PF = [0,0,0] 
            EW = [255,255,255]
            ECr = random.randint(0, 150)
            EC = [ECr,ECr,ECr]
            BCr = random.randint(0, 150)
            BC = [BCr,BCr,BCr]
            OT = [0,0,0]
            BG = [248, 240, 227]
            BKr = random.randint(0,150)
            BK = [BKr,BKr,BKr]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK
        
        # color generator for classified rarity
        def classified_wht(data, rarity):
            PF = [0,0,0] 
            EW = [80,80,80]
            ECr = random.randint(120, 200)
            EC = [ECr,ECr,ECr]
            BCr = random.randint(120, 210)
            BC = [BCr,BCr,BCr]
            OT = [255,255,255]
            BG = [28,28,28]
            BKr = random.randint(160,210)
            BK = [BKr,BKr,BKr]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK)
            return PF, EW, EC, BC, OT, BG, BK



        # img generator
        def img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK):        
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
            img_data.save(f'{PATH}/duck-{i+1}.png')
            img_data.show()

            # array used later to display how many of each rarity duck was generated
            rarity_array.append(i+1)
            rarity_array.append(rarity)
            
        rarity(data)

    rarity(data)

    rarity_display(rarity_array)



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



# procedure used to display how many ducks of each rarity was generated
def rarity_display(rarity_array):
    common = 0
    uncommon = 0
    rare = 0
    legendary = 0
    classified = 0
    
    print(rarity_array)

    for i in range(len(rarity_array)):
        if rarity_array[i] == 'common':
            common += 1
        elif rarity_array[i] == 'uncommon':
            uncommon += 1
        elif rarity_array[i] == 'rare':
            rare += 1
        elif rarity_array[i] == 'legendary':
            legendary += 1
        elif rarity_array[i] == 'classified':
            classified += 1

    print(f'common: {common}\nuncommon: {uncommon}\nrare: {rare}\nlegendary: {legendary}\nclassified: {classified}\n')


    
if __name__ == '__main__':
    main_loop()
    