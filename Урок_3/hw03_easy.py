__author__ = 'Николаев Александр Вадимович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) > 0.5:
        number = number // 1 + 1
    else:
        number = number // 1
    return number / (10 ** ndigits)


def my_round1(number, ndigits):
    number = number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)


print(my_round(2.1234567, 5))
print(my_round(-2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.9999927, 5))

print(my_round1(2.1234567, 5))
print(my_round1(-2.1999967, 5))
print(my_round1(2.9999967, 5))
print(my_round1(2.9999927, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    n = list(str(ticket_number))
    l = len(n)
    if l != 6:
        return 'Ошибка! номер билета не шестизначный'
    s1 = 0
    s2 = 0
    for i in range(l // 2):
        s1 += int(n[i])
        s2 += int(n[i + l // 2])
    if s1 == s2:
        return 'Да'
    else:
        return 'Нет'


print(f'Билет 123006 счастливый? - {lucky_ticket(123006)}')
print(f'Билет 12321 счастливый? - {lucky_ticket(12321)}')
print(f'Билет 436751 счастливый? - {lucky_ticket(436751)}')
