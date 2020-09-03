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

def bubblesort(lat):

    found = False
    sorted_index = len(lat) - 1

    while not found:
        found = True

        for i in range(sorted_index):

            if lat[i] > lat[i + 1]:
                store = lat[i + 1]
                lat[i + 1] = lat[i]
                lat[i] = store
                found = False

        sorted_index -= 1

if __name__ == '__main__':
    bubblesort(lat)
    print(lat)

