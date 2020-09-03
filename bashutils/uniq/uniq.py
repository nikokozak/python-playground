#! /usr/bin/python3

# Tiny implementation of uniq

import io
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('subject', default=sys.stdin, nargs='?', help="File or stdin")

args = parser.parse_args()

store = [] #incrementally store occurences of atom

if isinstance(args.subject, io.IOBase):
    text = args.subject.read().split('\n')
    print('\n')
    for line in text:
        if not line in store:
            store.append(line)
            print(line)
        else:
            pass
else:
    with open(args.subject) as of:
        for line in of:
            if not line in store:
                store.append(line)
                print(line, end='')
            else:
                pass
