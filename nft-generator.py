def image_file_to_array():
    image_array = []

    file = open('image_data.txt', 'r')

    file.strip(" ")
    lines = file.readlines()
    for line in lines:
        image_array = image_array.append(line.split(","))

    file.close()
    
    print(image_array)

if __name__ == '__main__':
    image_file_to_array()




