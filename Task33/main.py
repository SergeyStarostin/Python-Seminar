'''
Задача №37.
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
'''
number = int(input('Введите '))
def return_list(number: int) -> None:
    print(number)
    if number > 0:
        return_list(number - 1)
return_list(number)
