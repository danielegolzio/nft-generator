import numpy as np
import random
from PIL import Image

def file_to_array():
    file = open('image_data.txt', 'r')
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
    file.close()
    
    rarity(data)
    return data


def rarity(data, rarity):
    number = random.randint(1, 1000)
    if number >= 1 and number <= 500: # 50% chance of getting this rarity
        rarity = 'common'
    
    if number >= 500 and number <= 750: # 25% chance of getting this rarity
        rarity = 'uncommon'

    if number >= 750 and number <= 850: # 10 % chance of getting this rarity
        rarity = 'rare'
    
    

    art_generator(data, rarity)
    return rarity


def art_generator(data, rarity):
    for i in 50: # main loop for generating art
        pass



if __name__ == '__main__':
    file_to_array()
    