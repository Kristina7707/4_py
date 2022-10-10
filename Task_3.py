# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
lst = []
for i in range(10):
    lst.append(random.randint(1, 10))
print(lst)
newlst = []
for i in lst:
    if lst.count(i) < 2:
        newlst.append(i)
print(newlst)