#!/usr/bin/python

import os

path = 'c:\\projects\\hc2\\'
def printAllLines(dataDir):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))