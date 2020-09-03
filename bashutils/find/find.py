#!/usr/bin/python3

# 45-min implementation of find bin.

import os
from stat import S_ISREG, S_ISDIR, S_ISCHR, S_ISBLK, S_ISFIFO, S_ISLNK, S_ISSOCK, S_ISPORT
import argparse
import glob
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('dir', type=str, nargs=1)
parser.add_argument('-n', '--name', type=str, nargs=1, default='*')
parser.add_argument('-e', '--exec', type=str, nargs='+', dest='exe')
parser.add_argument('-t', '--type', type=str, nargs=1)

args = parser.parse_args()

def checkTypeFactory(method):
    def checkType(var):
        return method(var)
    return checkType

types = {
        'b': checkTypeFactory(S_ISBLK),
        'c': checkTypeFactory(S_ISCHR),
        'd': checkTypeFactory(S_ISDIR),
        'p': checkTypeFactory(S_ISFIFO),
        'f': checkTypeFactory(S_ISREG),
        'l': checkTypeFactory(S_ISLNK),
        's': checkTypeFactory(S_ISSOCK),
        }

path = os.getcwd()

files = glob.glob(args.name[0])

outputAfterTests = False

for f in files:

    mode = os.stat(path + '/' + f).st_mode
    istype = True

    if args.type:

        checker = types[args.type[0]]
        istype = checker(mode)

    if args.exe and istype:

        print(f)
        command = [ f if cmmd == '{}' else cmmd for cmmd in args.exe ]
        subprocess.run(command)
        outputAfterTests = True
    
    elif istype:

        print(f)
        outputAfterTests = True

if not outputAfterTests:
    print('No files found :(')
        
