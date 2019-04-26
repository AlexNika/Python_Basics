__author__ = 'Николаев Александр Вадимович'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def my_fibo(n, m):
    f1, f2 = 1, 1
    f_list = [1, ]

    for i in range(m):
        f1, f2 = f2, f1 + f2
        f_list.append(f1)

    return f_list[n - 1:m]


n, m = map(int, input('Введите n и m элементы ряда: ').split())
print(f'Функция Фибоначчи: {my_fibo(n, m)}')

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    a = 0
    b = 1
    while b < len(origin_list):
        while a < (len(origin_list) - 1):
            if origin_list[a] > origin_list[a+1]:
                origin_list[a], origin_list[a+1] = origin_list[a+1], origin_list[a]
            a += 1
        b += 1
        a = 0
    return origin_list

my_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(f'Оригинальный список: {my_list}')
new_list = sort_to_max(my_list)
print(f'Отсортированный по возрастанию список: {new_list}')

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(f, list_):
    res_list_ = []
    for i in range(len(list_)):
        if f(list_[i]):
            res_list_.append(list_[i])
    return res_list_


my_list = [131, 'tuple', 176, '', 2.778, 'float']
print(f'Оригинальный список, который надо отфильтровать: {my_list}')
print(f'С помощью своего фильтра выводим только элементы типа строка: {my_filter(lambda x: type(x) == str, my_list)}')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False


a1 = [0,0]
a2 = [30, 10]
a3 = [40, 40]
a4 = [10, 30]
print(f'Точки (0,0), (30, 10), (40, 40), (10, 30) являются вершинами параллелограмма? {is_parallelogram(a1,a2,a3,a4)}')
