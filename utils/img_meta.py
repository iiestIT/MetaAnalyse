import exifread

def img_meta(img_input):
    with open(img_input, "rb") as img:
        tags = exifread.process_file(img)

    return tags
