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

def selectsort(lat):

    pointer = 0
    lowest = lat[pointer]
    toswitch = 0

    while pointer < len(lat):

        lowest = lat[pointer]

        for i in range(pointer + 1, len(lat)):

            if lat[i] < lowest:

                toswitch = i
                lowest = lat[i]

        if i != pointer:
            store = lat[toswitch]
            lat[toswitch] = lat[pointer]
            lat[pointer] = store
        pointer += 1

    
if __name__ == '__main__':
    selectsort(lat)
    print(lat)


