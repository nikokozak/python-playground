import random



def bubblesort(lat):
    found = False
    while not found:
        found = True
        counter = 1
        while counter < len(lat):
            if lat[counter - 1] > lat[counter]:
                store = lat[counter - 1]
                lat[counter - 1] = lat[counter]
                lat[counter] = store
                found = False
            counter += 1
    return lat

def maketest():
    lat = []
    for i in range(1000):
        lat.append(random.randrange(1000))
    return lat

testlat = maketest()
print(bubblesort(testlat))
            
