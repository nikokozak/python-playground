import argparse
import sys
import io

parser = argparse.ArgumentParser()
parser.add_argument('stream', default=sys.stdin, nargs='*', type=int, help="String of space separated integers if piped, else space separated integers.")
args = parser.parse_args()

lat = []

if isinstance(args.stream, io.IOBase):
    
    lat = args.stream.read().split(' ')
    lat = [int(x) for x in lat if len(x) > 0]

else:

    lat = args.stream 

def insertsort(lat):

    pointer = 1

    for i in range(pointer, len(lat)):

        tempval = lat[pointer]

        while lat[pointer - 1] > tempval and (pointer - 1) >= 0:

            store = lat[pointer - 1]
            lat[pointer - 1] = lat[pointer]
            lat[pointer] = store

            pointer -= 1

        pointer = i + 1

if __name__ == '__main__':
    insertsort(lat)
    print(lat)

        

