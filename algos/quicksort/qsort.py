def swap(val1, val2, lat):
    store = lat[val1]
    lat[val1] = lat[val2]
    lat[val2] = store

def pivot(low, high, lat):

    if len(lat) > 1:

        pivot = high - 1
        largest = 0
        pointer = 0

        while pointer < pivot and largest < pivot: 
            
            while lat[pointer] >= lat[pivot]: 
                pointer += 1

            while lat[largest] < lat[pivot]:
                largest += 1
                pointer += 1

            if pointer > largest and pointer != pivot:
                swap(pointer, largest, lat)
                largest += 1

            
        swap(largest, pivot, lat)
        return largest

    return 0

def quicksort(low, high, lat):

    if low < high:

        j = pivot(low, high, lat)
        quicksort(low, j, lat)
        quicksort(j + 1, high, lat)

lat = [0, 3, 6, 19, 2, 8, 5, 3]

quicksort(0, len(lat), lat)