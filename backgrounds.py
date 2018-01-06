# -*- coding: utf-8 -*-
import os
from PIL import Image
from shutil import copy

def getSourceDir():
    temp = os.path.join(
        os.environ['LOCALAPPDATA'].__str__(),
        'Packages')
    find = 'Microsoft.Windows.ContentDeliveryManager'
    target = [dirname for dirname in os.listdir(temp) if dirname.startswith(find)][0]

    return os.path.join(
        temp,
        target,
        'LocalState',
        'Assets')

def getDestDir():
    return os.path.join(
        os.environ['USERPROFILE'].__str__(),
        'Pictures',
        'AutoBackgrounds')

def makeDestDir(dest):
    try:
        os.mkdir(dest)
    except FileExistsError:
        pass

def getBaseFileNames(dir):
    return [name.split('.')[0] for name in os.listdir(dir)]

def cleanFolder(dest):
    files_to_delete = list()
    count = 0
    deleted = 0
    for file in os.listdir(dest):
        try:
            # Using PIL module to get the pic dimensions
            im = Image.open(os.path.join(dest,file))
            # this checks that the pic is in landscape and has horizonal size greater than 1000 pixels
            if (im.size[0] < im.size[1]) or im.size[0] < 1000:
                count += 1
                files_to_delete.append(file)
        except OSError:
            count += 1
            files_to_delete.append(file)
    for file in files_to_delete:
        try:
            os.remove(os.path.join(dest,file))
            deleted += 1
        except:
            # sometimes a photo is blocked, this let's you know
            print('couldnt delete ',file)
    return deleted


if __name__ == "__main__":
    # this only works on Windows
    assert os.environ['OS'] == 'Windows_NT'
    
    # need the source and destination directories; make destination if necessary
    source = getSourceDir()
    dest = getDestDir()
    makeDestDir(dest)
    
    # create lists of files in source and destination directories
    src_file_names = os.listdir(source)
    dest_file_names = getBaseFileNames(dest)

    # find source files that are not already in our backgrounds folder
    screened = [file for file in src_file_names if os.path.getsize(os.path.join(source,file)) > 500000]
    no_duplicates = [file for file in screened if file not in dest_file_names]

    # copy file names from source to destination
    print(str(len(no_duplicates)) + ' items moved')
    for f in no_duplicates:
        src = source + '\\' + f
        pic = dest + '\\' + f + '.bmp'
        copy(src,pic)
    # clean up unwanted pics
    pics_deleted = cleanFolder(dest)
    print("items deleted: ",str(pics_deleted))
