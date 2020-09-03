#!/usr/bin/python3

# 45-min implementation of cat bin.

import fs
import argparse
import os

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-n', '--number', action='store_true', help='Display numbers')
group.add_argument('-b', '--number-nonblank', action='store_true', help='Number only nonblank lines', dest='nonblank')

parser.add_argument('-E', '--show-ends', action='store_true', help='Show line ends', dest='ends')
parser.add_argument('f', nargs='+', type=str, help='Filename or path to file')

args = parser.parse_args()

root = fs.open_fs('/')
wd = (os.getcwd() + '/')[1:]

append = '$' if args.ends else ''

for f in args.f:

    path = wd + f

    try:
        with root.open(path) as of:
            linecount = 0
            for index, line in enumerate(of):
                if args.number:
                    print(str(index) + ' ' + line.rstrip() + append)
                elif args.nonblank:
                    if not line.isspace():
                        print(str(linecount) + ' ' + line.rstrip() + append)
                        linecount += 1
                else:
                    print(line.rstrip() + append)
                        
    except fs.errors.ResourceNotFound as e:
        print('cat: ' + f + ': No such filename')
        
