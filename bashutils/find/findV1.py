#!/usr/bin/python3
import fs 
import argparse
import glob
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('dir', type=str, default='.', help='Dir in which to look')
parser.add_argument('-n', '--name', type=str, default='', help='Glob or name to find')
parser.add_argument('-e', '--exec', type=str, nargs='+', dest='exe', help='Command to execute on file')

args = parser.parse_args()

path = args.dir + '/' + args.name

matches = glob.glob(path)

root = fs.open_fs(args.dir)
info = root.getinfo(args.name, namespaces=['details'])
print(info.type == 2)

if not args.exe:
    for f in matches:
        print(f)
else:
    for f in matches:
        command = [f if cmmd == '{}' else cmmd for cmmd in args.exe]
        print(f)
        try:
            subprocess.run(command)
        except:
            print("There was an error running the specified command.")
    


