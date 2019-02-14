from os import listdir
from os.path import isfile,join

# Directory for files list to be reoganized
dirPath = '/Volumes/FSA_IMAGES/1935/'

# Generate filesList, print size
print('Generating filesList .... ')
filesList = listdir(dirPath)
print('filesList size =',len(filesList))



for file in filesList:
