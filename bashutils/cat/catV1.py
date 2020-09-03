#!/bin/python3

# CONCATENATE FILES AND PRINT

# If no file or - read standard input and copy to output

# -n, --number - output line nums
# -E, --show-ends - display $ at end of line
# -b, --number-nonblank - override n and output only nonblank line nums
# -s, --squeeze-blank - suppress repeated empty output lines

import fs
import argparse
import sys

parser = argparse.ArgumentParser()

# ADD ARGS HERE

# CONFLICTING OPTIONAL
conflictopt = parser.add_mutually_exclusive_group()
conflictopt.add_argument('-n', '--number', action='store_true', help="Display line numbers")    
conflictopt.add_argument('-b', '--number-nonblank', action='store_true', dest='nonblank')
conflictopt.add_argument('-s', '--squeeze-blank', action='store_true', dest='squeeze')

parser.add_argument('-E', '--show-ends', action='store_true', dest='ends')
parser.add_argument('f', type=str, nargs='*', default=sys.stdin, help="Files to read, alternatively stdin")


args = parser.parse_args()

# ADD LOGIC HERE

wd = fs.open_fs('.')

append = '$' if args.ends else '' 

for f in args.f:
    try:
        with wd.open(f) as open_f:
            
            if (args.number):
                for index, line in enumerate(open_f):
                    print(str(index) + ' ' + line.rstrip() + append)
            elif (args.nonblank):
                counter = 0
                for index, line in enumerate(open_f):
                    if not line.isspace():
                        print(str(counter) + ' ' + line.rstrip() + append)
                        counter += 1 
            elif (args.squeeze):
                for index, line in enumerate(open_f):
                    if not line.isspace():
                        print(line.rstrip() + append)
            else:
                for index, line in enumerate(open_f):
                    print(line.rstrip() + append)

    except fs.errors.ResourceNotFound as e:
        print('cat: ' + f.rstrip() + ': No such file or directory')
 
