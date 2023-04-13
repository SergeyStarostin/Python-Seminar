"""
Задача №11
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""
number = int(input('Номер элемента ряда Фибоначчи: '))
first = 0
second = 1
current = 0
index = 0
while second < number:
    current = first + second
    second = first
    first = current
    index += 1
if second == number:
    print(f'Число Фибоначчи {number} является {index} по счету')
else:
    print(f'Число {number} не является числом Фибоначчи')