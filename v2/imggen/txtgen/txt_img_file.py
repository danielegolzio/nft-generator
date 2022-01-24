# turns the txt file contianing the image data into a list
def txt_img_file():
    # turns image_data file into a list
    file = open('imggen/txtgen/image_data/image_data.txt', 'r')
    # new array that contains all RGB pixel values
    data = [line.strip('\n')[:-1].split(',') if line[-2] == ',' else line.strip('\n').split(',') for line in file.readlines()] # made by Royce Chan
    file.close()

    return data