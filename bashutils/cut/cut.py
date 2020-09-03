#!/usr/bin/python3

#45 Min implementation of cut

import argparse
import sys
import io

parser = argparse.ArgumentParser()

parser.add_argument('subject', type=str, nargs='*', default=sys.stdin) 
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--characters', type=str)
group.add_argument('-f', '--fields', type=str)

args = parser.parse_args()

def getInOut(arglist):
    cutin = 0
    cutout = 0

    if len(arglist) >= 3:
        args = arglist.split('-')
        cutin = args[0]
        cutout = args[1]
    elif len(arglist) == 2:
        if arglist[0] == '-':
            args = arglist.split('-')
            cutin = None;
            cutout = args[0]
        elif arglist[1] == '-':
            args = arglist.split('-')
            cutin = args[0]
            cutout = None;
        else:
            raise ValueError("There was a problem parsing your in out points")
    elif len(arglist) == 1:
        cutin = arglist[0]
        cutout = int(cutin) + 1

    return (int(cutin), int(cutout))
            

if isinstance(args.subject, io.IOBase):

    if args.characters:

        cutin, cutout = getInOut(args.characters)
        chars = [x for x in args.subject.read()]
        print("".join(chars[cutin:cutout]))

    elif args.fields:

        cutin, cutout = getInOut(args.fields)
        fields = args.subject.read().split()
        print(" ".join(fields[cutin:cutout]))

    else:
        print(args.subject.read())

else:
    
    cutin = 0
    cutout = None


    for f in args.subject:

        with open(f) as of:

            text = of.read()

            if args.characters:
                cutin, cutout = getInOut(args.characters)
                print(text[cutin:cutout])

            elif args.fields:
                cutin, cutout = getInOut(args.fields)
                text = text.split()
                print(text[cutin:cutout])

            else:
                print(text)


            

