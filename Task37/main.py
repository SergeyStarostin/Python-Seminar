'''
Задача №37.
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
number_N = int(input('Введите число: '))
def revers_list(number_N: int) -> str: #функция возвращает строчное значение
    if number_N == 0:
        return ''
    return f'{number_N} ' + revers_list(number_N - 1)
print(revers_list(number_N))