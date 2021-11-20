from PIL import Image
from numpy import asarray

def image_data():
    image_name = input('file name: ')
    image = Image.open(image_name)
    data = asarray(image)

    image_data_file(data)
    return data


def image_data_file(data):
    file = open('image_data.txt', 'w')

    for i in range(30):
        for j in range(30):

            R, G, B = data[i][j]

            if (R,G,B) == (0, 0, 0):
                file.write('PF')

            elif (R,G,B) == (255, 255, 255):
                file.write('EW')

            elif (R,G,B) == (255, 0, 0):
                file.write('EC')

            elif (R,G,B) == (200, 200, 200):
                file.write('BC')

            elif (R,G,B) == (50, 50, 50):
                file.write('OT')
            
            elif (R,G,B) == (0, 0, 255):
                file.write('BG')
            elif (R,G,B) == (0, 255, 0):
                file.write('BK')

            if i != 30 and j != 29:
                file.write(',')

        if i != 30 and j != 30:
            file.write('\n')
        
    file.close()


if __name__ == '__main__':
    image_data()