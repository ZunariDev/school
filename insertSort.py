import time
import random

listNum = [i+1 for i in range(int(input("List length [-> int] > ")))]
random.shuffle(listNum)

def insertSort(item):
    for i in range(1, len(item)):
        print(f"DEBUG: for loop executed with i = {i}")
        j = i
        loop = True
        
        while j > 0:
            print(f"DEBUG: while loop executed with j = {j}")
            print(f"DEBUG: {item[j]}")
            
            if item[j] < item[j-1]:
                item[j], item[j-1] = item[j-1], item[j]
            else:
                break
            
            j -= 1

print(listNum)
insertSort(listNum)
print(listNum)