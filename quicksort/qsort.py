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

def swap(val1, val2, lat):
    store = lat[val1]
    lat[val1] = lat[val2]
    lat[val2] = store

def pivot(low, high, lat):

    pivot = lat[high - 1]
    high = high - 2
    low = low 
    
    while True:

        while lat[high] >= pivot and high >= low:
            high -= 1

        while lat[low] <= pivot and high >= low:
            low += 1

        if high >= low:
            swap(high, low, lat)
        else:
            break

    swap(low, high-1, lat)

    return high

def quicksort(low, high, lat):

    if low < high:

        j = pivot(low, high, lat)
        quicksort(low, j + 1, lat)
        quicksort(j + 1, high, lat)

if __name__ == '__main__':
    pivot(0, len(lat), lat)
    print(lat)







