# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:27:38 2025

@author: ПользовательHP
"""
from random import randint

arrA = []
print("Введите границы интервала,в которых будут находится значения: ")
minA = int(input("От:"))
maxA = int(input("До:"))

print("Введите количество элементов: ")
count = int(input())

for i in range(count):
    arrA.append(randint(minA, maxA))

summ=0
even=[]

for i in arrA:
    if (i%2 == 0):
        even.append(i)
        
for i in even:
    summ += i

print(summ)
   
