import os
import shutil
import zipfile

folder = r"C:\Users\dstan\Documents\testing\ziprenametesting"
#var equals scandir checks contents of folder and returns directories only as a list
#this for loop pattern is basically variable equals result of the for loop, iterated
subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
pgnum = 0

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
