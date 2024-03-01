from os import listdir, makedirs, chdir
from os.path import isfile,join
from shutil import copy2 as copy
from Spinner import Spinner
import csv

# Directory for files list to be reoganized
srcPath = '/media/pete/FSA_IMAGES/1935_/'
tgtPath = '/media/pete/FSA_IMAGES/1935/'
#srcPath = '/home/pete/School/SeniorProject/150px/'
#tgtPath = '/home/pete/School/SeniorProject/150px_/'

# Generate filesList, print size
print('Generating filesList .... ')
filesList = listdir(srcPath)
print('filesList size =', len(filesList))

# start spinner
spinner = Spinner()
spinner.start()

# Change into path directory
chdir(srcPath)

# create parent directories:
parentDirs = ["jpg_150_Preview", "jpg_r_Small", "jpg_v_Large", "tif_u_Small",
              "tif_a_Large", "other"]
for dir in parentDirs:
    try:
        makedirs(tgtPath+dir)
    except FileExistsError: 
        pass

# array of 'bad' files:
badFiles = []

# copy files to new location:
for file in filesList:
    try:
        id = file[7]
        if id == '_':
            copy(file, tgtPath+parentDirs[0])
        elif id == 'r':
            copy(file, tgtPath+parentDirs[1])
        elif id == 'v':
            copy(file, tgtPath+parentDirs[2])
        elif id == 'u':
            copy(file, tgtPath+parentDirs[3])
        elif id == 'a':
            copy(file, tgtPath+parentDirs[4])
        else:
            copy(file, tgtPath+parentDirs[5])
    except IndexError:
        badFiles.append(file)

if badFiles:
    try:
        with open(tgtPath+'badCopies.csv','w',newline='') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            wr.writerow(badFiles)
    except OSError:
        print(badFiles)

# terminate spinner
spinner.stop()
