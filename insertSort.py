import time
import random

listNum = [i+1 for i in range(int(input("List length [-> int] > ")))]
random.shuffle(listNum)

def insertSort(item):
    for i in range(1, len(item)):
        j = i
        loop = True
        
        while j > 0:
            if item[j] < item[j-1]:
                item[j], item[j-1] = item[j-1], item[j]
            else:
                break
            
            j -= 1

print(listNum)
time1 = time.time()
insertSort(listNum)
time2 = time.time()
print(listNum)
print(f"Sort time: {round(time2 - time1, 4)}")
