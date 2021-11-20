def image_file_to_array():
    array = []

    file = open('image_data.txt', 'r')

    lines = file.readlines()
    for line in lines:
        array = array.append(line.split(","))

    file.close()
    
    print(array)

if __name__ == '__main__':
    image_file_to_array()




