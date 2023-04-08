""""
Задача №1.

За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output: 2
"""

distanceDay = int (input ('Введите расстояние за 1 день: '))
totalDistance = int (input ('Введите расстояние: '))
numberOfDays = (distanceDay - 1 + totalDistance) // distanceDay
print(f'Машина проедет {totalDistance} км за {numberOfDays} дня')