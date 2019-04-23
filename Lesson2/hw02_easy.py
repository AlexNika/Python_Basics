# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
my_fruits = ['яблоко', 'банан', 'киви', 'арбуз']
# ###
# ### Вариант №1
# ###
for i, value in enumerate(my_fruits, 1):
    print(f'{i}. {value:>6}')
print()
# ###
# ### Вариант №2
# ###
for i in range(len(my_fruits)):
    print('{}. {:>6}'.format(i + 1, my_fruits[i]))
    

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
from random import randint
# ###
# ### Генерируем список случайных чисел, случайной длины
# ###
while True:
    random_list1 = [randint(0, 100) for i in range(randint(0, 100))]
    random_list2 = [randint(0, 100) for i in range(randint(0, 100))]
    l1 = len(random_list1)
    l2 = len(random_list2)
    if l1 != 0 or l2 != 0:
        print(f'Список №1 случайных целых чисел: {random_list1}')
        print(f'Список №2 случайных целых чисел: {random_list2}', '\n')
        break
    else:
        print('Генератор создал пустой список. Пробуем еще раз')
print(f'Длина исходного списка №1 = {l1}', '\n')
# ###
# ### Удаляем из списка №1 числа присутсвующие в списке №2
# ###
flag = False
for each in random_list2:
    c = random_list1.count(each)
    if c >= 1:
        flag = True
        for i in range(0, c):
            random_list1.remove(each)
            print(f'Из списка №1 удалено число {each}')
l1 = len(random_list1)
if flag:
    print(f'Список №1 с удаленнымы числами списка №2: {random_list1}', '\n')
    print(f'Теперь длина списка №1 = {l1}')
else:
    print('В списке №1 нет чисел из списка №2')


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
from random import randint
# ###
# ### Генерируем список случайных чисел, случайной длины
# ###
while True:
    random_list = [randint(-100, 100) for i in range(randint(0, 20))]
    l = len(random_list)
    if l != 0:
        print(f'Список случайных целых чисел: {random_list}')
        break
    else:
        print('Генератор создал пустой список. Пробуем еще раз')
new_list = []
for each in random_list:
    if each % 2 == 0:
        new_list.append(each / 4)
    else:
        new_list.append(each * 2)
print(f'Новый список: {new_list}')
