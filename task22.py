# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов 1го множества: '))
m = int(input('Введите количество элементов 2го множества: '))

def FillList(num):
    import random
    list_i = []
    for i in range(num):
        list_i.append(random.randint(0, 20))
    return list_i

list_1 = FillList(n)
list_2 = FillList(m)
set_1=set(list_1)
set_2=set(list_2)

result = set_1.intersection(set_2)
print(list_1, list_2, result, sep = '\n')

