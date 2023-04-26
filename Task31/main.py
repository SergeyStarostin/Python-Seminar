''''
Задача №31.
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи. Задание необходимо решать через рекурсию.
Input: 7
Output: 21
'''
def fibo(number):
    if number in [0, 1]:
        return number
    return fibo(number - 1) + fibo(number - 2)
number = int(input('Введите число: '))
print(f'{number}-й элемент последовательности Фибоначчи = {fibo(number)}')
