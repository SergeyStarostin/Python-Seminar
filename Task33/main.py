'''
Задача №33.
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
import random

list_score = []
evaluations = int(input('Введите количество оценок: '))
for i in range(evaluations):
    list_score.append(random.randint(1, 5))
print(f'Список оценок: {list_score}')
max_point = max(list_score)
min_point = min(list_score)
for i in range(evaluations):
    if list_score[i] == max_point:
        list_score[i] = min_point
print(f'Исправленные оценки: {list_score}')