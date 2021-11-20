def file_to_array():
    array2d = []
    
    file = open('image_data.txt', 'r')
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

    
    for i in list(lines):
        array2d.append(list(i))
    
    print(array2d)

    file.close()
    


if __name__ == '__main__':
    file_to_array()
    