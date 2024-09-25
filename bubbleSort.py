import random
import time

listNum = [i+1 for i in range(int(input("List length [-> int] > ")))]
random.shuffle(listNum)

def sort(item):
    for i in range(1, len(item)):
        for i in range(len(item) - 1):
            if item[i] > item[i+1]:
                item[i], item[i+1] = item[i+1], item[i]

print(listNum)
timeStart = time.time()
sort(listNum)
timeEnd = time.time()
print(listNum)
print(f"Sort time: {round(timeEnd - timeStart, 4)}")
