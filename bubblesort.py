import random
import time

list = [i+1 for i in range(500)]
random.shuffle(list)

def swap(list, i1, i2):
    list[i1], list[i2] = list[i2], list [i1]

def sort(list):
    count = len(list) - 1
    counter = 1

    while counter <= len(list):
        for i in range(count):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
            #print(list)
        counter += 1
        count -= 1

print(list)
timeStart = time.time()
sort(list)
timeEnd = time.time()
print(list)
print(f"Sorting took {round(timeEnd - timeStart, 4)} seconds.")