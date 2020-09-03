#!/usr/bin/python3

# 20 minute implementation of grep

import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('regex', nargs=1, type=str, help='pattern to match')
parser.add_argument('searchfile', nargs='+', type=str, help='file to look in')

parser.add_argument('-i', '--ignore-case', dest='ignore', action='store_true', help='ignore case')

args = parser.parse_args()

if args.ignore:
    prog = re.compile(args.regex[0], re.I)
else:
    prog = re.compile(args.regex[0])

files = args.searchfile

found_something = False

for sf in files:

    results = []

    with open(sf) as f:

        for line in f:
            match = prog.search(line)

            if match:

               results.append(line)

    if results:
        found_something = True
        print(sf + ': ')
        for result in results:
            print(result)

if not found_something:
    print('No results found')
