#! /usr/bin/python3

# Merge Sort

# 1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# 2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.


# [9, 8, 7, 6, 5, 4, 3, 2, 1]
# [9], [8], [6], [5], [4], [3], [2], [1]
# [8, 9], [5, 6], [3, 4], [1, 2]
# [5, 6, 8, 9], [1, 2, 3, 4]
# [...]
import random

def mergesort(lat):

    if len(lat) <= 1:
        return lat

    mid = len(lat) // 2
    left = lat[:mid]
    right = lat[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(a, b):

    if not b:
        return a

    result = []

    i = j = 0 

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1

    return result

def maketest():
    result = []
    for i in range(1000):
        result.append(random.randrange(1000))
    return result

test = maketest()
print(mergesort(test))

