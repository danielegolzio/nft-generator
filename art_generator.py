import numpy as np
import random
from PIL import Image, ImageOps
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

    # turns christmas_image_data file into a list
    christmas_file = open('image_data_christmas.txt', 'r')
    # new array that contains all RGB pixel values
    christmas_data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in christmas_file.readlines()] # also made by Royce Chan
    christmas_file.close()

    # main loop
    for i in range(0, loop_counter):
        
        # rarity generator
        def rarity(data, christmas_data):
            number = random.randint(1, 10000)
                    
            # 50% chance of getting this rarity
            if number >= 1 and number <= 5000:
                rarity = 'common'
                common(data, rarity, christmas_data)
                return rarity
                    
            # 25% chance of getting this rarity
            elif number >= 5000 and number <= 7500:
                rarity = 'uncommon'
                uncommon(data, rarity, christmas_data)
                return rarity

            # 15% chance of getting this rarity
            elif number >= 7500 and number <= 9000:
                rarity = 'rare'
                rare(data, rarity, christmas_data)
                return rarity

            # 2% chance of getting this rarity
            elif number >= 9000 and number <= 9200:
                rarity = 'legendary'
                main_colors = 'red'
                legendary_r(data, rarity, christmas_data)
                return rarity

            # 2% chance of getting this rarity
            elif number >= 9200 and number <= 9400:
                rarity = 'legendary'
                main_colors = 'green'
                legendary_g(data, rarity, christmas_data)
                return rarity

            # 2% chance of getting this rarity
            elif number >= 9400 and number <= 9600:
                rarity = 'legendary'
                main_colors = 'blue'
                legendary_b(data, rarity, christmas_data)
                return rarity

            # 1% chance of getting this rarity
            elif number >= 9600 and number <= 9700:
                rarity = 'classified'
                main_colors = 'black'
                classified_blk(data, rarity, christmas_data)
                return rarity

            # 1% chance of getting this rarity
            elif number >= 9700 and number <= 9800:
                rarity = 'classified'
                main_colors = 'white'
                classified_wht(data, rarity, christmas_data)
                return rarity

            # 0.1% chance of getting this rarity
            elif number >= 9700 and number <= 9710:
                rarity = 'Holiday'
                main_colors = 'Christmas'
                holiday_christmas(data, rarity, christmas_data)
                return rarity

            # 0.01% chance of getting this rarity
            elif number == 10000:
                rarity = 'upside down'
                upsidedown(data, rarity, christmas_data)
                return rarity
            
            # this is here untill all 10000 numbers are occupied by a rarity
            else:
                rarity = 'common'
                common(data, rarity, christmas_data)
                return rarity



        # color generator for common rarity
        def common(data, rarity, christmas_data):
            PF = [0,0,0]
            EW = [255,255,255]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
        
        # color generator for uncommon rarity
        def uncommon(data, rarity, christmas_data):
            PF = [0,0,0]
            EW = [0,0,0]
            EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
            BG = [250,249,213]
            BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
        
        # color generator for rare rarity
        def rare(data, rarity, christmas_data): # later on this will get complementary colors...
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [0,0,0]
            EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [255-EC[0],255-EC[1],255-EC[2]]
            BG = [250,249,213]
            BK = [255-BC[0],255-BC[1],255-BC[2]]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH

        # color generator for legendary rarity
        def legendary_r(data, rarity, christmas_data):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [random.randint(50, 255),0,0]
            BC = [random.randint(50, 255),0,0]
            OT = [random.randint(100, 250),0,0]
            BG = [random.randint(1, 255),0,0]
            BK = [random.randint(50, 255),0,0]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
        
        # color generator for legendary rarity
        def legendary_g(data, rarity, christmas_data):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [0,random.randint(50, 255),0]
            BC = [0,random.randint(50, 255),0]
            OT = [0,random.randint(100, 255),0]
            BG = [0,random.randint(1, 255),0]
            BK = [0,random.randint(50, 255),0]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
        
        # color generator for legendary rarity
        def legendary_b(data, rarity, christmas_data):
            eyeWhiteColors = [255,0]
            eyeWhite = random.choice(eyeWhiteColors)
            PF = [0,0,0] 
            EW = [eyeWhite,eyeWhite,eyeWhite]
            EC = [0,0,random.randint(50, 255)]
            BC = [0,0,random.randint(50, 255)]
            OT = [0,0,random.randint(100, 250)]
            BG = [0,0,random.randint(1, 255)]
            BK = [0,0,random.randint(50, 255)]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH

        # color generator for classified rarity
        def classified_blk(data, rarity, christmas_data):
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
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
        
        # color generator for classified rarity
        def classified_wht(data, rarity, christmas_data):
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
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH

        def holiday_christmas(data, rarity, christmas_data):
            PF = [0,0,0] 
            EW = [255,255,255]
            EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [255-EC[0],255-EC[1],255-EC[2]]
            BG = [250,249,213]
            BK = [255-BC[0],255-BC[1],255-BC[2]]
            CH = [255, 0, 0]

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
            

        def upsidedown(data, rarity, christmas_data):
            PF = [0,0,0] 
            EW = [0,0,0]
            EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
            BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
            OT = [255-EC[0],255-EC[1],255-EC[2]]
            BG = [250,249,213]
            BK = [255-BC[0],255-BC[1],255-BC[2]]
            CH = None

            img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data)
            return PF, EW, EC, BC, OT, BG, BK, CH
            


        # img generator
        def img_generator(data, rarity, PF, EW, EC, BC, OT, BG, BK, CH, christmas_data):        
            RGB_data = []

            # makes a new array replacing the letters with the generated RGB colors
            if rarity != 'Christmas':
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
            else:
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
                

            # new dimensions for image
            dimensions = 480,480

            # array handling with numpy
            RGB_data = np.array(RGB_data, dtype=np.uint8)
            RGB_data = RGB_data.reshape(30,30,3)
            
            # using PIL to turn the RGB values into an image
            img_data = Image.fromarray(RGB_data, 'RGB')
            img_data = img_data.resize(dimensions, resample=0)

            # flips image if its upside down rarity
            if rarity == 'upside down':
                img_data = ImageOps.flip(img_data)

            img_data.save(f'{PATH}/duck-{i+1}.png')

            # array used later to display how many of each rarity duck was generated
            rarity_array.append(i+1)
            rarity_array.append(rarity)
            
        rarity(data, christmas_data)

    rarity(data, christmas_data)

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
    christmas = 0
    upsidedown = 0
    
    # print(rarity_array)

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
        elif rarity_array[i] == 'christmas':
            christmas += 1
        elif rarity_array[i] == 'upside down':
            upsidedown += 1

    print(f'\ncommon: {common}\nuncommon: {uncommon}\nrare: {rare}\nlegendary: {legendary}\nclassified: {classified}\nchristmas: {christmas}\nupside down: {upsidedown}\n')


    
if __name__ == '__main__':
    main_loop()
    