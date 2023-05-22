'''
Lambda
В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
'''
def select(function, value):
    return [function(x) for x in value]

def where(function, value):
    return [x for x in value if function(x)]

print('Список чисел: ', data := [1, 2, 3, 5, 8, 15, 23, 38])

result = select(int, data)

print('Список четных чисел: ', result := where(lambda x: x % 2 == 0, result))

print('Список четных чисел: ', result := list(select(lambda x: (x, x ** 2), result)))