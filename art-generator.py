def file_to_array():
    file = open('image_data.txt', 'r')
    data = file.read()
    for i in data:
        i.replace('\n', ' ')
    
    print([data.split(',')])

    file.close()
    

if __name__ == '__main__':
    file_to_array()
    