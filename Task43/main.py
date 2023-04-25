'''
Задача №43.
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод:
1 2 3 2 3
Вывод:
2
'''
import random

print(my_list := [random.randint(0, 10) for _ in range(10)])
print(sum([my_list.count(i) // 2 for i in set(my_list)]))