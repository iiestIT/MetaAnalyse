import exifread
import datetime
import json
import os


def data(img_input, name="default"):
    now = datetime.datetime.now()
    date_time = now.strftime("%H-%M-%S_%m-%d-%Y")
    
    img = open(img_input, "rb")
    tags = exifread.process_file(img)
    tags.update({'time_now' : date_time})
    tags.update({'file_name' : name})

    for key, value in tags.items():
        print(str(key) + ": " + str(value))

    try:
        with open("cache.txt", "w") as file:
            file.write("cache_dict" + " = " + str(tags))

            
            
    except IOError:
        print(IOError)

'''
with open("test.jpg", "rb") as img:
    tags = exifread.process_file(img)
    for key, value in tags.items():
        print(str(key) + " - " + str(value))
        '''

data('test.jpg')

"""
def data(img_input):
    img = open(img_input, "rb")
    tags = exifread.process_file(img)
    try:
        for key, value in tags.items():
            print(str(key) + " - " + str(value))
            
    except IOError:
        print("Error")"""