#imports
import sys
import os
from os import listdir, remove
from os.path import isfile, join, exists

def writeFile(list):
    path = os.path.abspath(filepath) + ".new"
    with open(path, 'a') as writer:
        for content in list:
            writer.write(content + "\n")
    writer.close()

def getFilename():
    return filepath.split('/')[len(filepath.split('/')) -1 ]

#check length
if(len(sys.argv) <= 1):
    print("Error: You must supply a file to parse in the arguments.")
    exit()

argument_length = len(sys.argv)
filepath = sys.argv[1]
anyfile = False
if(sys.argv.__contains__("--anyfile")):
    anyfile = True

if(isfile(filepath) == False):
    print("Error: File is not a regular file.")
    exit()

split = filepath.split('.')
if(split[(len(split) - 1)] != "txt" and anyfile != True):
    print("Error: Supplied file must be a text file. (Ignore this with --anyfile)")
    exit()

finallist = list()
duplicatecount = 0

for string in open(filepath, 'r').readlines():
    if(finallist.__contains__(string)):
        duplicatecount += 1
    else:
        finallist.append(string)

writeFile(finallist)
print("Done. Duplicates found: " + str(duplicatecount))