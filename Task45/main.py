'''
Задача №45.
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1,
но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите
все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
не превосходящее 10000. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
(перестановка чисел новую пару не дает).
Ввод:
300
Вывод:
220 284
'''
def sun_dividers(number: int) -> int:
    sum_div = 0
    for div in range(1, number // 2 + 1):
        if number % div == 0:
            sum_div += div
    return sum_div
number_k = int(input(f'Введи диапазон: '))
for num in range(number_k):
    if num == sun_dividers(sun_dividers(num)) and num < sun_dividers(num):
        print(num, sun_dividers(num), sep=' \U0001F91D ')