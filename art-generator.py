
import numpy as np
import random
from PIL import Image


def file_to_array(): # turns image_data file into a list
    file = open('image_data.txt', 'r')
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
    file.close()
    print(data)
    
    rarity(data)
    return data


def rarity(data): # generates rarity for image
    number = random.randint(1, 1000)
    if number >= 1 and number <= 500: # 50% chance of getting this rarity
        rarity = 'common'
    
    elif number >= 500 and number <= 750: # 25% chance of getting this rarity
        rarity = 'uncommon'

    elif number >= 750 and number <= 850: # 10% chance of getting this rarity
        rarity = 'rare'
    
    elif number >= 850 and number <= 900: # 5% chance of getting this rarity
        rarity = 'covert'
    
    elif number >= 950 and number <= 960: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'red'

    elif number >= 960 and number <= 970: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'green'

    elif number >= 970 and number <= 980: # 1% chance of getting this rarity
        rarity = 'legendary'
        main_colors = 'blue'

    elif number == 999: # 0.1% chance of getting this rarity
        rarity = 'classified'
        main_colors = 'black'
    
    elif number == 1000: # 0.1% chance of getting this rarity
        rarity = 'classified'
        main_colors = 'white'


    art_generator(data, rarity)
    return rarity


def art_generator(data, rarity):
    for i in range(50): # main loop for generating art
        pass



if __name__ == '__main__':
    file_to_array()
    