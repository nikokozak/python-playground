#!/usr/bin/python3

# Tiny impl. of sed

import sys
import io
import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source', default=sys.stdin, nargs='?', help='input')
parser.add_argument('-e', '--expression', type=str, help='expression')

args = parser.parse_args()

def parseReg(reg): # Parse our expression argument string --> returns tuple

    analysis = re.findall("/", reg)

    if len(analysis) < 3:
        raise ValueError("An input and replacement strings are needed: /xx/XX/")

    if not reg:
        raise ValueError("An expression is required!")
    
    if not reg[0] == 's':
        raise ValueError("Currently only strings are supported: s/XXX/XXX/[g]")

    parts = reg.split('/')

    tosub = parts[1]
    toins = parts[2]

    flags = parts[3] if len(parts) > 2 else None
    multi = True if flags and re.match("g", flags) else False 
    ignoreCase = True if flags and re.match("i", flags) else False 

    return (tosub, toins, multi, ignoreCase)

tosub, toins, multi, ignoreCase = parseReg(args.expression)

re.purge() # Clear cache

if isinstance(args.source, io.IOBase):
    text = args.source.read().split('\n')
    for line in text:
        print(re.sub(tosub, toins, line, count=False if multi else 1, flags=re.I if multi else False), end='\n')
else:
    with open(args.source) as of:
        for line in of:
            print(re.sub(tosub, toins, line, count=False if multi else 1, flags=re.I if multi else False), end='')
