import time
import random

listNum = [i+1 for i in range(int(input("List length [-> int] > ")))]
random.shuffle(listNum)

def selectSort(item):
    for i in range(len(item)):
        value = item[i]
        valueIndex = i
        for j in range(i+1, len(item)):
            if value > item[j]:
                value = item[j]
                valueIndex = j
        
        item[i], item[valueIndex] = item[valueIndex], value[i]
    
print(listNum)
time1 = time.time()
selectSort(listNum)
time2 = time.time()
print(listNum)
print(f"Sort time: {round(time2 - time1, 4)}")
