#? imports
import exifread, datetime, os, copy

# ? main-function
def data(img_input, name="default"):
    if name == "default":
        name = img_input

    now = datetime.datetime.now()                                                                               #? get a timestamp
    date_time = now.strftime("%H-%M-%S_%m-%d-%Y")                                                               #? timestamp-format = h, m, s - m, d, y
    
    cache_dir = "./cache/exifread/"                                                                             #? cache directory (path)
    path_name = name + "_" + date_time                                                                          #? filename + timestamp = path-name
    path = os.path.join(cache_dir, path_name)                                                                   #? path = cach_dir + path_name
    
    img = open(img_input, "rb")                                                                                 #? open input in b as img
    tags = exifread.process_file(img)                                                                           #? read the exif-data and create a dict named tags
    tags.update({'time_now' : date_time})                                                                       #? timestamp is joyning the dict
    tags.update({'file_name' : name})                                                                           #? filename is joyning the dict

    try:
        JPEGThumbnail = copy.deepcopy(tags["JPEGThumbnail"])                                                    #? JPEGThumbnail is copyed from the dict if it exist
        if JPEGThumbnail:
            with open(path + "_" + "JPEGThumbnail.txt", "w") as thumbnail:                                      #? write the JPEGThumbnail in the cache folder as an own file if is exist
                thumbnail.write(str(JPEGThumbnail))
            del tags["JPEGThumbnail"]
    except:
        print("JPEGThumbnail not exist" + " " + name + "_" + date_time)

    try:
        with open(path + ".json", "a") as file:                                                                 #? create the json file with path + .json
            file.write("{" + "\n")                                                                              #? write the first line of json-format
            for key, value in tags.items():                                                                     #? loop the dict tags and write it into the file
                if key != "file_name":                                                                          #? TRUE for all vals exept file_name
                    file.write("    " + '"' + str(key) + '"' + " : " + '"' + str(value) + '",' + "\n")          #? format of the lines

                else:                                                                                           #? only file_name
                    file.write("    " + '"' + str(key) + '"' + " : " + '"' + str(value) + '"' + "\n")           #? same like above without the last ,
            file.write("}" + "\n")                                                                              #? last character in the json-format

    except IOError:                                                                                             #TODO write a errorhandler
        print(IOError)

data("20140622_124126.jpg")