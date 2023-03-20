# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
import math

array = []
n = int(input("Введите длину массива: "))
for i in range(n):
    array.append(randint(1, 10))

number = int(input("Введите искомое число: "))
difference = 10
memory = 0

for i in range(len(array)):
    if (math.sqrt((array[i] - number) * (array[i] - number)) < difference):
        memori = array[i]
        difference = array[i] - number

print(array)
print(f"Ближайшее число к числу {number} это {memori}")