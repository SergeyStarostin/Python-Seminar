'''
Задача №31.
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''
number = int(input('Введите число: '))
def fibonacci(number):
    if number in (0, 1):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)
print(fibonacci(number))
