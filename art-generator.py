def file_to_array():
    file = open('image_data.txt', 'r')
    data = file.read()
    data_array = data.split(',')

    for i in data:
        if i == '\n':
            data.remove(i)

    print(data_array)

    file.close()
    

if __name__ == '__main__':
    file_to_array()
    