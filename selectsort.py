import time
import random

liste = [i+1 for i in range(int(input("List length [int] > ")))]
random.shuffle(liste)

def swap(list: list, ind1: int, ind2: int):
    list[ind1], list[ind2] = list[ind2], list[ind1]

def selectSort(liste):
    for i in range(len(liste)):
        value = liste[i]
        valueIndex = i
        for j in range(i+1, len(liste)):
            if value > liste[j]:
                value = liste[j]
                valueIndex = j
        
        swap(liste, i, valueIndex)
    
print(liste)
time1 = time.time()
selectSort(liste)
time2 = time.time()
print(liste)
print(f"Sorting took {round(time2 - time1, 4)} seconds.")