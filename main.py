# name = 'Maks'
# print("Hello, ", name)
# print(type(name))
# a = 4
# b = 5
# print(id(a))
# name = input('Ваше имя')
# city = input('Москва слезам не верит')
# print('Грод',name, 'name', city)
# import locale
# import time
# num = int(input('Введите число'))
# st = int(input('Введите степень'))
# a = num ** st
# print('Чисо:',a,'\n Вы гений, ура!!!<3' )
# print('***Введите полтора цифры***')
#
# a = int(input('First: '))
# b = int(input('Second: '))
# c = int(input('Third: '))
# d = int(input('4: '))
# num = (a + b) / (c + d)
# print('Результат:', num)
# import re
# import shlex

# print(bool(''))

# a = int(input('Первая сторона'))
# b = int(input('Вторая сторона'))
# c = int(input('Третья сторона'))
# if a == b == c:
#     print('Треугольник равносторнний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')


# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 10
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# a, b = 2, 0
# print("На ноль делить нельзя" if b == 0 else a / b)
#
#

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Код далее")
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
# print()
# ...


# n = int(input('Введите первое число: '))
# m = int(input('Введите второе число: '))
# try:
#     n = int(n)
#     m = int(m)
#     print(n + m)
# except ValueError:
#     n= str(n)
#     m = str(m)
# print(n + m)


# i = 0
# while i < 5:
#     print('i=', i)
#     i +=1

#######################################
# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое!')
#         n = input('Введите целое число:')
#
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end='@#$%')
#     if i == 5:
#         break
#
#     i+=1
# print('\nЦикл завершен!')


# while True:
#     n = input(int("Введите положительоне число"))
#     if n > 0:
#         break

# n = int(input('Введите любое число: '))
# count = 1
# while n != 0:
#     count *= n
#     int(input('Введите любое число: '))
# print('Произведение чисел:', count)


# res = 1
# while True:
#     n = int(input(" введите число: "))
#     if n == 0:
#         print("результат:", res)
#         break
#     res = res * n

# i = 0
# while i < 1238652:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i= ", i)


# i = 1
# while i < 5:
#     print('Внешний цикл i = ', i)
#     j = 1
#     while j < 4:
#         print('\tВнешний цикл: j =', j)
#         j += 1
#     i += 1


# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i +=1

# for i in 'Hello':
#     print(i)
#
# i = 1
# for color in 'red', 'orange', 'blue':
#     print(i, "color:", color, type(color))
# i += 1

# for i in range(n):
#     Тело цикла

# range(start, stop, step)


# for i in range(9):
#     print(i, end=' ')
#

# for i in range(0, 110, 10):
#     print(i, end=' ')


# a = int(input('Введите целое число: '))
# for i in range(1, a+1):
#     if a % i == 0:
#         print(i)

# a = str(input('Введите прикол'))
# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i)

# for i in range(3):
#     print(i)
#     # if i == 2:
#     #     break
# else:
#     print('done')


# for i in range(2):
#     print('+++')
#     for j in range(8):
#         print("-----")

# i = 0
# a = int(input('Введите ширину  прямоугольника: '))
# b = int(input('Введите высотy прямоугольника: '))
# for i in range(b):
#         print('*'*a)
#         i += 1

# i = 0
# a = int(input('Введите ширину  прямоугольника: '))
# b = int(input('Введите высотy прямоугольника: '))
# for i in range(a):
#     print(0, a)
#     for j in range(b):
#         if 0 < i < a - 1 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")

# a = [letter * 5 for letter in 'Hello']
# print(a)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# num = [8, 7, 'one', [1, 2, 3, 4, 5]]
# # print(num)
# # print(type(num))
# # print(num[1])
# # print(num[-1][1])
# # num[2] = 245
# # print(num)
# # num[1] += 100
#
# print('Dlina spiska: ', len(num))

# s = []
# print(type(s))
# b = list('Hello')
# print(b)

# a = [5, 2] * 6
# print(a)

# n = list(range(-2, 10, 2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n +1)]
# print(a)
#
# a = [1, 2 ,3 ,4]
# b = [5, 6, 7]
# c = a + b
# print(c)

# a = [0] * int(input('dfgdfgd: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('->'))
# print(a)

# b = [0, 0, 0]
# b[0] = 5
# b[1] = 6
# b[2] = 7

# a = [input('->') for i in range(int(input('kol-vo elementov: ')))]
# print(a)

# a = [4, 5, 6, 3, 2]
# for i in range(len(a)):
#     print(a[i], end='')

# list = ['one', 'two', 'three']
# for i in list:
#     print(i, end=' ')

# count = 0
# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# for i in a:
#     if i < 0:
#         count += 1
# print('Сумма отрицательных элементов:', count)
#
# s = 0
# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# for elem in a:
#     if elem < 0:
#         s += elem
# print(s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print('kol-vo ch: ', k)
# print('kol-vo nech: ', s)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# res = 0
# sumk = 0
# for i in a:
#     if i != 0:
#         res += 1
#         sumk += i
# print(sumk/res)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i])

# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# for i in range(len(a)):
#     if a[(i-1)] < a[i]:
#         print(a[i])
#     i +=1
# s = [2, 3, 4, 5, ]
# s.extend([9, 8, 7])#множество append только один элем
# print(s)

# s.insert(1, 100) #добовляет заданное значение 2параметр по указанному индексу 1параметр

# lst = []
# n = int(input('Кол-во элементов списка: '))
# for num in range(n):
#     x = int(input('Введите ччисло: '))
#     lst.append(x)
# print(lst)

# a = [5, 6, 3, 3, 1, 4, 4, 2, 3]
# b = [4, 3, 2, 1, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)
#

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)
#

# s = [5, 6, 3, 3, 1, 4, 4, 2, 3]
# #s[4:] = []
# s.remove(0)
# print(s)

# print(dir(list))


# s = [5, 6, 3, 3, 1, 4, 4, 2, 3]
# ind = s.index(3, 3) #что ищем с какого индекса до какого
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy() #копия списка
# print('a=', a)
# print('b=', b)
# print('s_copy=', s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print('a=', a)
# print('b=', b)
# print('s_copy=', s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))
#
#
# s = [5, 6, 3, 3, 1, 4, 4, 2, 3]
# s.reverse()
# print(s)
# s.sort(reverse=True)
# print(s)
#
# s2 = ['dfvd', 'sd', 'sdf']
# s2.sort(key=len)
# print(s2)
# srt = sorted(s)
# print(srt)

# import random as r

# from random import randint, randrange
# from random import *
# # print(r.random())
# # print(randint(10, 92))
# print(randrange(0, 10, 2))
# print(round(uniform(10.5, 25.5), 2))
#
# s = [55, 44, 324, 23, 78] #какое-то значение из списка не разбираясь
# print(choice(s))
# print(choices(s, k=10))
# shuffle(s)
# print(s)
#
# mas = [randint(0, 100) for i in range(0, 10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# lst = ['a', 'one', 'red', 'home']
# print(len(lst))
# # print(sum(lst))
# print(min(lst))
# print(max(lst))

# from random import randint, randrange


# mas = [randint(0, 100) for i in range(0, 10)]
# print(mas)
# a = max(mas)
# print(max(mas))
# mas.remove(a)
# mas.insert(0, a)
# print(mas)

# lst = [randint(-20, 20) for i in range(0, 10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(0, 10)]
# print(lst)
# m = min(lst)
# print(m)
# l = lst.index(m)
# print(l)
# del lst[:l]
# print(lst)

# x = list('12hj14g1')
# print(x)
# print('a' in x)

# lst = []
# print(bool(lst))
# if not lst:
#     print('Список пустой^u^')

# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# c = a + b
# print('Третий список: ', c)
# c = []
# for i in range(len(a)):
#     if a[i]not in c:
#         c.append(a[i])
# for j in range(len(b)):
#     if b[j]not in c:
#         c.append(b[j])
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# # print(m)
# # print(m[1][2])
# #
# # for row in range(len(m)):
# #     for col in range(len(m[row])):
# #         print(m[row][col])
#
# for row in m:
#     for x in row:
#         print(x, end='\t\t')
#     print()
# print()
# for row in m:
#     for x in row:
#         print((x ** 2), end='\t\t')
#     print()

# k = 1
# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x != 0:
#             k *= x
#         print(x, end='\t\t')
#     print()
# print('Колво отрицатедьных:', k)

# import time
# second = time.time()
# print('Количсетво секунд с начала эпохи: ', second)
# localtime = time.ctime(11)
# print(localtime)
# res = time.localtime(second)
# print(res)
# print(time.strftime('Today is %B %d, %Y'))
# print(time.strftime('%m/%d/%Y, %H:%M:%S', time.localtime(12313121412)))
#
# pause = 5
# print('Program strted..')
# time.sleep(pause)
# print(pause, 'seconds')
#
# text = input('Название напоминания: ')
# locale_time = float(input('Через сколько min:'))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Today is %B %d, %Y'))

# def hello(name, word):
#     print('Hello', name, word)
#
#
# hello('mama', 'hi')
# hello('papa', 'hello')
# def get_summ(a, b):
#     print(a+b)
#
#
# x = 2
# y = 4
# get_summ(x, y)
# n = 7
# m = 8
# get_summ(n, m)
# get_summ('qwe', 'rty')

# def simb(count, a, b):
#     for i in range(count):
#         if i % 2 !=0:
#             print(a)
#         else:
#             print(b)
#
#
# simb(9, '+', '-')
# simb(7, 'X', 'O')

# def get_summ(a, b):
#     return a + b
#
#
# x = 2
# y = 3
# res = get_summ(x, y)
# print(res)

# one = int(input())
# two = int(input())
# def maximum(one, two):
#     if one > two:
#         return one - two
#     elif two > one:
#         return two + one
#
#
# print(maximum(one, two))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]\
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(234, 3))
# print(is_greater(4, 34))

# def check_password(password):
#     hes_upper = False
#     hes_down = False
#     hes_num = False
#
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             hes_upper = True
#         elif 'a' <= ch <= 'z':
#             hes_down = True
#         elif '0' <= ch <= '9':
#             hes_num = True
#
#     if len(password) >= 8 and hes_upper and hes_down:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('yeeeeeeeeeeees!!5*&&#(&')
# else:
#     print('NO.')

# def get_summ(a, b, c=0, d=1):
#     return a + b + c + d
#
# q = 2
# print(get_summ(2, 4, 5))
# print(get_summ(2, 4, d=2))

# def g(simbol):
#     return simbol * 20
#
#
# print(g('-'))
# print(g(simbol='+'))
# print(g(simbol='='))
# print(g('-'))

# def digit_sum(n, even = True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
#
# print('Сумма четных цифр: ')
# print(digit_sum(2423424))
# print(digit_sum(24232424))
# print(digit_sum(2423424244))
# print('Сумма нечетных цифр: ')
# print(digit_sum(24234249, even=False))
# print(digit_sum(242324245, even=False))
# print(digit_sum(24234242447, even=False))

# def displayinfo(name, age):
#     print('name: ', name, '\nage: ', age)
#
#
#
# displayinfo('ira', 23)
# displayinfo(age=23, name='ira')

# =-================================================
# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# row = 0
# for row in lst:
#     for col in lst:
#         print(col, end='\t')
#     print()
# print('-----------------------')
# i = 0
# for col in row:
#     for row in lst:
#         print(row[i], end='\t')
#     i += 1
#     print()


# a = {0, 1, 'vova', 2, 'masha',  3}
# a.add(4)
# a.remove('vova')
# print(a)
# a.discard('1') #удалит элемент если таквой есть. иначе ничего не происходит


# a = {0, 1, 2, 3}
# b = {1, 2, 3, 4}
# # c = a.union(b)
# # c = a| b
# # a |= b
# # a &= b
# # c = a - b
# c = a ^ b
# print(c)

# s1 = {1, 2 }
# s2 = {3}
# s3 = {4 ,5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = 'Hello'
# s2 = 'How are u'
# s = set(s1) & set(s2)
# print(s)

# s1 = 'Python'
# s2 = 'Programming langueg'
#
# s = set(s1) - set(s2)
# print(s)

# s1 = {'marina', 'sveta', 'jenya'}
# s2 = {'kostya', 'jenya', 'ilya'}
# only = s1 ^ s2
# print(only)
# both = s1 & s2
# print(both)

# a = frozenset([1, 2, 3, 4])
# print(a)


# d = {'one': 1, 'two': 2}
# d1 = dict(one=1, two=2)

# a = [
#     ('igorgmail.com', 'igor'),
#     ('bulbash@gmail.com', 'bulbash'),
#     ('anngma', 'anna')
# ]
# d = dict(a)
# print(d)

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# if 3 in d:
#   print(true)
#
#
# key = 'one'
#   del d[key]
# try:
#     del d[key]
# except KeyError:
#     print('//', key, )

# for key in d:
#     print(key)

# sl = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# d = sl['x1'] * sl['x2'] * sl['x3'] * sl['x4']
# print(d)

# d = {a: input('-->') for a in range(1, 5)}
# # d[1] = input('-->')
# # d[2] = input('-->')
# # d[3] = input('-->')
# # d[4] = input('-->')
# print(d)
# a = int(input('Какой элемент исключить? '))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print('Такого элемента нет')

# goods = {
#     '1': [' Core-i3-4330', 9, 4500],
#     '2': [' Core-i5-4670k', 9, 4500],
#     '3': [' AMD fix 6300', 9, 4500],
#     '4': [' Pentium G3220', 9, 4500],
#     '5': [' Core-i5-3450', 9, 4500]
# }
#
#
# for i in goods:
#     print(i, ')', goods[i][0], '-', goods[i][1], ' шт. по ', goods[i][2], 'руб',  sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         cnt = int(input('Kol-vo: '))
#         goods[n][1] = cnt
#     else:
#         break


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b')
# print(value)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value = d.values()
# print(value)
#
# for i in d: #.values()
#     print(i)

# for i, j in d.items():
#     print(i, j)

# d2 = d
# d2 = d.copy()
# d2['a'] = 7
# print(d)
# print(d2)


# # list()
# figures = {1: 'rectangle', 2: 'treangle', 3: 'circle'}
# # value = list(figures)
# value = list(figures.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip()

# d = dict(zip([12, 1, 2], ['dec', 'jan', 'feb']))
# print(d)


# a = [12, 1, 2]
# b = ['dec', 'jan', 'feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)


# a = [1, 2, 3]
# print(list(zip(a)))
#
#
# print(list(zip(range(5), range(100))))

# a = {'name': 'Igor', 'surname': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Masha', 'surname': 'Pupok', 'job': 'Consultant'}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, v1)
#     print(k2, v2)

# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)


# month = ['Jan', 'Feb', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, production_cost, month):
#     res = sales - cost
#     print('Xbcnfz ghb,skm', m, '=', res)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, v)

# en = ['red ', 'green', 'blue']
# for j, i in enumerate(en, 1):
#     print(j, i)

# en = {0: 1, 1: 2, 2: 3}
# for i, j in enumerate(en, 1):
#     print(i, ':', j, '->', en[j])

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
#
# print(func(1))
# print(func(1, 2))

# def summa(*parasm):
#     res = 0
#     for i in parasm:
#         res += 1
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)

# def predict(*args):
#     return {i: i for i in args}
#
#
# print(predict(1, 2, 3, 4))
# print(predict('grey', (2, 17), 3.11, -4))

# def print_scores(stud, *scores):
#     print('Student name: ', stud)
#     for score in scores:
#         print(score, end=' ')
#     print()
#
#
# print_scores('Jhonatan', 100,99,89, 95)
# print_scores('Bedol', 20, 12, 32, 70)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(a='Python'))
# print(func())

# def info(**data):
#     for k, v in data.items():
#         print(k, v)
#     print('8'*20)
#
# info(first_name='ira',  last='bgd',prisgf='29375982365' )
# info(first_name='dgd',  last='asfg3',prisgf='29371245982365', emaul='bhsdg@SDG')

# оюасть видимости scope()
# for i in range(4):
#     print(i)
# print(i)

# name = 'Tom'
#
#
# def hi():
#     print('Hello', name)
#
#
#
# def bye():
#     global name
#     name = 'Bob'
#     print('Bye', name)
#
#
# hi()
# bye()
# print(name)


# def outer_func():
#     def inner_func():
#         print('hello')
#     inner_func()
#
#
# outer_func()


# def func1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print(a + b)
#
#     print(a)
#     func2(4)
#
#
# func1()


# x = 25
#
#
# def f():
#     global t
#     a = 30
#
#     print(x)
#
#     def innner():
#         nonlocal a
#         a = 35
#         print(a)
#
#
#     innner()
#     t = a
#
# f()
# z = x + t
# print(z)


# замыкания


# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# res = outer(5)
# print(res(10))
#
#
# res2 = outer(7)
# print(res2)


# def f1():
#     a = 1
#     b = 'Line'
#     c = [1, 2, 3]
#
#     def f2():
#         nonlocal a
#         c.append(4)
#         a += 1
#         return a, b, c
#
#     return f2
#
#
# func = f1()
# print(func)


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('сочи')
# res2()
# res2()
# res2()

#
# students = {
#     'ali': 67,
#     'masha': 88,
#     'dima': 1,
#     'vova':100
#
# }
#
# def make_classifier(lower, upper):
#     def classify_students(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper }
#
#     return classify_students
#
#
# a = make_classifier(80, 101)
# b = make_classifier(70, 80)
# c = make_classifier(40, 70)
# d = make_classifier(0, 40)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def f(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def nul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.nul = nul
#     return replace
#
#
# ob1 = f(5, 2)
# print(ob1.add())


# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
#
# func = (lambda x, y: x + y)('a', 'b')
# print(func)
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda n: (lambda x: (lambda z: x + n + z)))(2)(3)(4))

# players = [{'name': 'Антон', 'last_name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last_name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last_name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last_name': 'Семенов', 'raiting': 6}]
#
# res = sorted(players, key=lambda item: item['last_name'])
# print(res)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y)]
# b = a[0](12, 4)
# print(b)


# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# mystr = 'Test string for me'
# arr = [ord(x) for x in mystr]
# print(arr)
# arr = [sum(arr) // len(arr)] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in (input('->'))[:3]] if x not in arr]
# print(arr)

# a = 122
# b=97
# for i in range(b, a+1):
#     print(chr(i), end=' ')

# from random import randint
#
# shortest = 7
# longest = 10
# min_acsiii = 33
# max_aciii = 126
#
#
# def randompas():
#     random_length = randint(shortest, longest)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(min_acsiii, max_aciii))
#         res += random_char
#     return res
#
#
# print('Ваш случайный пароль: ', randompas())

# s = 'Hello, WORLD! I am learning Python.'
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.swapcase())  # hELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
#
# print(s.count('l', 3))
# print(s.find('Python'))


# a = 'один два'
# b = a[:a.find(' ')]
# c = a[a.find(' ')+1:]
# print(c + ' ' + b)

# a = 'ab12c59p7dq'
# digits = []
#
# for i in a:
#     if i in '1234567890':
#         digits.append(int(i))
# print(digits)
#
# print(s.index('Python'))
# print('py'.center(10))


# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык програмирования.'
# print(st)
# print(st.replace('Nython', 'Python', 2))

# s = '-|-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print('..'.join(['1', '2']))

# print('sdgfs sdafs asfa'.split())
# print('sdgfs_sdafs_asfa'.split('s'))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = input('->').split()
# print(a)

# a = list(map(int, input('->').split()))
# print(a)

# a = input('Введите ФИО: ').split()
# print(a)
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')

# import re
#
# # s = 'Я ищу совпадения в 2023 году. И я их найду в два счёта.'
# # reg = 'я'
# # print(re.findall(reg, s))
# # print(re.search(reg, s))
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).group())
#
# # print(re.split(reg, s))
#
# # s = 'Я ищу 2совпадения в 3 году. И я их найду1 в два счёта.'
# # reg = r'\d'
# # print(re.split(reg, s))
#
#
# # s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# # reg = r'\.'
# # print(re.split(reg, s, 1))
# # print(re.sub(reg, '!', s, 1))
#
# # s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# # reg = r'[0-9]'
# # reg = r'[12][09][0-9][0-9]'
# # print(re.findall(reg, s))
#
# # s1 =  'Час в 24=часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапозоне от 00 до 59. 2121-06-Т01:09'
# # pattern = '[0-2][0-9]:[0-5][0-9]'
# # print(re.findall(pattern, s1))
#
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# # reg = r'[^0-9]'
# # reg = r'\w'
# # reg = r'\d'
# reg = r'\A\w\s\w+'
# reg = r'\S'
# print(re.findall(reg, s))


import re


# s1 = 'Цифры: 7, +17, -42, 0013, 0.3'
# pattern = r'[+-]?\d+[.\d]*'
# print(re.findall(pattern, s1))


# s1 = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'#.*', '', s1))
# print('Дата рождения:', re.sub(r'-?#.*', '.', s1)[:-1])
# print(re.sub(r''))


# s1 = 'author=Пушкин А. С.; title = Евгений Онегин; price =200; year= 1831'
# pattern = r'\w+\s*=\s*[^;]+'
# print(re.findall(pattern, s1))

# s1 = '12 сентября 2021 года'
# reg1 = r'\d{2,4}'
# print(re.findall(reg1, s1))


# def login(a):
#     return re.findall(r'^[\w!@#$-]{8, 25}$', a)
#
#
# print(login('admin_admin'))
# print(login('*admin_admin'))


# text = '''
# one
# two
# '''
# print(re.findall(r'one$', text, re.MULTILINE))

# print(re.findall('''[A-z.-]+@[a-z_.-]+''', 'test@gmail.com'))



# s = 'Hello, world!'
# print(re.findall(r'\w+', s, re.DEBUG))

# text = '''Python,
# python,
# PYTHON
# '''
# reg = r'(?im)^python'
# print(re.findall(reg, text))  # flags=re.MULTILINE | re.IGNORECASE

# s = '12345@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# reg = r'[\w.-]+@[\w\.]+[^., ]'
# print(re.findall(reg, s))

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.+?>', text))
#
# # *?, +?, ??
# # {m, n}?, {,n}?, {m,}?
#
# t = '2324 786 22 4569'
# reg = r'\d{1,3}?'
# print(re.findall(reg, t))
#
# s = '<p>Изображение<img src="bg.jpg"> - фон страницы</p>'
# reg = r'<img\s+[^>]*>'
# print(re.findall(reg, s))


# s = 'Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19].'
# reg = r'\[\d+?\]+'
# print(re.findall(reg, s))

# s = 'Петр и Ольга отлично учаться!'
# reg = 'Петр|Ольга|koko'
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# reg = r'(?:int|double)\s+=\s+\d[.\w+]*'
# # reg = r'int\s+=\s+\d[.\w+]*|double\s+=\s+\d[.\w+]*'
# print(re.findall(reg, s))

# s = '127.0.0.1'
# reg = r'(?:\d{1,3}\.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

#
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


print('hello')