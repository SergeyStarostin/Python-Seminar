'''
Map
В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
'''
def where(function, collection):
    return [x for x in collection if function(x)]

print('Список: ', data := '1 2 3 5 8 15 23 38'.split())

result = map(int, data)

print('Список четных чисел: ', result := where(lambda x: x % 2 == 0, result))

print('Список пар чисел: ', result := list(map(lambda x: (x, x ** 2), result)))