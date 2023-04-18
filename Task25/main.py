'''
Задача №25.
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
'''
my_list = input('Введите строку из элементов через пробел: ').split()
dict_count = {}
for letter in my_list:
	if letter in dict_count:
		print(f'{letter}_{dict_count[letter]}', end=' ')
	else:
		print(letter, end=' ')
	dict_count[letter] = dict_count.get(letter, 0) + 1