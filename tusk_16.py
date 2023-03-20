# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

array = []
n = int(input("Введите колличество элементов массива: "))

for i in range(n):
    array.append(randint(1, 10))


number = int(input("Введите число, которое необходимо найти: "))

count = 0

for i in range(len(array)):
    if (array[i] == number):
        count += 1

print(array)
print(f"Число {number} встречается {count} раз.")