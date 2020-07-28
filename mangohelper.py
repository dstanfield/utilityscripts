import os
import shutil
import zipfile

folder = r"C:\Users\dstan\Documents\testing\ziprenametesting"
pgnum = 0
zipex = ".zip"

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
        #extract it to the proper folder
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
