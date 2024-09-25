import random
import time

list = [i+1 for i in range(int(input("List length [-> int] > ")))]
random.shuffle(list)

def sort(item):
    for i in range(1, len(item)):
        for i in range(len(item) - 1):
            if item[i] > item[i+1]:
                item[i], item[i+1] = item[i+1], item[i]

print(list)
timeStart = time.time()
sort(list)
timeEnd = time.time()
print(list)
print(f"Sort time: {round(timeEnd - timeStart, 4)}")
