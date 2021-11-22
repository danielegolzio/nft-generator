import numpy as np
import random

def file_to_array():
    file = open('image_data.txt', 'r')
    data = [line.strip('\n')[:-1].split(',') if line[-2] == "," else line.strip('\n').split(',') for line in file.readlines()]
    file.close()
    
    color_generator(data)
    return data

def color_generator(data):
    pf = [0, 0, 0]
    

if __name__ == '__main__':
    file_to_array()
    