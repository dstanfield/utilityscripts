import os
import shutil
import zipfile
from argparse import ArgumentParser
import pathlib
import logging

logging.basicConfig(level=logging.DEBUG)

# Invoke the script like the following:
# python mangohelper.py --volume_number 7 --image_extension jpg --filepath ../path/to/my/mangoes/
parser = ArgumentParser()
parser.add_argument("--volume_number", type=int, help="Volume number of the mango")
parser.add_argument("--image_extension", choices=["jpg", "png"], help="Image extension of mangos")
parser.add_argument("--filepath", type=pathlib.WindowsPath, help="Filepath of folder containing mango chapters")
args = parser.parse_args()

# keeping these around in case I need them later
# logging.debug("Looking for items in folder {}".format(str(args.volume_number)))
# logging.debug("Looking for items in folder {}".format(str(args.image_extension)))
# logging.debug("Looking for items in folder {}".format(str(args.filepath)))

pgnum = 0
zipex = ".zip"
volumenumber = args.volume_number
#adding period here so the parser lines are cleaner
jaypeg = "." + str(args.image_extension)
folder = str(args.filepath) 

#change to directory with files
os.chdir(folder) 

#go through items in directory
for item in os.listdir(folder): 
    #if it's a zip
    if item.endswith(zipex): 
        #get the full path
        file_name = os.path.abspath(item) 
        #create a zipfile boi
        zip_ref = zipfile.ZipFile(file_name) 
        #extract that boi
        zip_ref.extractall(folder) 
        #close that boi
        zip_ref.close() 
        #credit to https://stackoverflow.com/questions/58792626/extract-all-files-from-multiple-folders-with-python
        
#var equals scandir checks contents of folder and returns directories only as a list
#this for loop pattern is basically variable equals result of the for loop, iterated
#has to be after extraction since there aren't directories until they're extracted
subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

#for folder in subfolder list
for sub in subfolders:
    #for item in subfolders (listdir only returns names, instead of scandir which returns lots of stuff)
    for f in os.listdir(sub):
        #source directory equals sub (subfolder path) plus f (item name)
        src = os.path.join(sub, f)
        #destination is folder aka main folder plus pgnum being inserted into var.jpg
        dst = os.path.join(folder, "{}.jpg".format(pgnum))
        #iterate
        pgnum += 1
        #copy over
        shutil.copy(src, dst)

#last step is to zip the images up, then change the filename from .zip to .cbz
 
#gather all the images
imgs = [f.path for f in os.scandir(folder) if f.path.endswith(jaypeg)]
#create the zip object, could do it inside the loop with append mode
zip_handler = zipfile.ZipFile(folder + "\\volumeout.zip", "w")
#loop through and add all the images
for i in imgs:
    zip_handler.write(os.path.join(folder, i))
#gotta close the ziphandler object for the file to write
zip_handler.close()

#rename to cbz
os.rename("volumeout.zip", "volume{}.cbz".format(volumenumber))

#delete all the objects created
for imgfolders in subfolders:
    shutil.rmtree(imgfolders)
#not very good at variable naming
for goaway in imgs:
    os.remove(goaway)








    
