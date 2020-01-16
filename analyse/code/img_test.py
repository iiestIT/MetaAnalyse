from PIL import Image, ExifTags
#import exifread
import os
import copy

def img_test(img_input):
    img = open(img_input, "rb")
    print(img)
    tags = exifread.process_file(img)
    print(str(tags))

    for key, value in tags.items():
        print(str(key) + " : " + str(value))

def pil_test(img_input):
    img = Image.open(img_input)

    for key, value in img:
        if key in ExifTags.TAGS:
            print(ExifTags.TAGS[key] + " : " + str(value))

pil_test("test2.jpg")