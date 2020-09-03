
def maketest():
    test = []
    for i in range(100):
        test.append(i)
    return test

def binsearch(val, lat):
    
    found = False
    upperbound = len(lat)
    lowerbound = 0
    middle = len(lat) // 2

    while lowerbound <= upperbound:
        if val > lat[middle]:
            lowerbound = middle
        elif val < lat[middle]:
            upperbound = middle
        elif val == lat[middle]:
            return middle
        middle = (upperbound + lowerbound) // 2
    
    return None 

test = maketest()
print(binsearch(80.5, test))
