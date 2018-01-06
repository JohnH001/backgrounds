# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 09:30:36 2017

@author: johnm
"""

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

def filesToMoveDictionary(src_files, dest_files, src_dir):
    #create a dictionary with files in source with a minimum size and not in destination
    MINIMUM = 300000
    dict_files = dict()
    for file in src_files:
        src_name = os.path.join(src_dir,file)
        src_size = os.path.getsize(src_name)
        if src_size >= MINIMUM and file not in dest_files:
            dict_files[file] = src_size
    return dict_files

def cleanFolder(dest):
    files_to_delete = list()
    count = 0
    deleted = 0
    for file in os.listdir(dest):
        try:
            im = Image.open(os.path.join(dest,file))
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
            print('couldnt delete ',file)
    return deleted


if __name__ == "__main__":
    # this only works on Windows
    # assert os.environ['OS'] == 'Windows_NT'
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

    # copy file names in dictionary from source to destination
    print(str(len(no_duplicates)) + ' items moved')
    for f in no_duplicates:
        src = source + '\\' + f
        pic = dest + '\\' + f + '.bmp'
        copy(src,pic)
    # clean up unwanted pics
    pics_deleted = cleanFolder(dest)
    print("items deleted: ",str(pics_deleted))
