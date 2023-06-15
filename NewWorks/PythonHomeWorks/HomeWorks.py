#  Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# a = (input('Введите трехзначное число: '))
# b = int (a[0])
# c = int (a[1])
# d = int (a[2])

# result = (b+c+d)
# print (result)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int (input('Введите общее число журавликов: '))
# if not s % 6:
#     x = s//6
# print (f'Катя сделала {x *4} корабликов')
# print (f'Петя сделала {x } корабликов')
# print (f'Сережа сделала {x} корабликов')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# while True:
#     number = input('Введите шестизначный номер Вашего билета: ')
#     if number.isdigit() and len(number) == 6:
#         if sum(map(int, number[:3])) == sum(map(int, number[3:])):
#             print('Yes')
#         else:
#             print('No')
#         break
#     else:
#         print('Введен некорректный номер билета, попробуй cнова')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите один размер шоколадки в дольках: "))
# m = int(input("Введите другой размер шоколадки в дольках: "))

# k = int(input("Введите количество долек, которое хотите отломить: "))

# if k < m * n and (k % m == 0 or k % n == 0):
#     print('Yes')
# else:
#     print('No')

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input())
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k<n/2 else n-k)

# Задача 12. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение .
# Помогите Кате отгадать задуманные Петей числа.

# s = int(input('Задай сумму двух чисел \n'))
# p = int(input('Задай произведение чисел \n'))
# for x in range(s):
#     for y in range(p):
#         if s == x + y and p == x * y:
#             print(f'первое число = {x}, второе число = {y}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. 

# n = int(input('Введи число N:'))
# i = 0
# while 2 ** i <= n:
#     print(f' 2 в степени {i} равна {2 ** i}')
#     i += 1    

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = int(input('Введите размер элементов списка: '))
# list_n = input('Введите элементы списка через пробел: ').split()
# arr = list(map(int, list_n))
# x = int (input('Введите число х: '))
# count = 0
# for i in range(n):
#     if arr[i] == x:
#         count += 1
# print(f'Число {x} встречается в списке А {count} раз.') 

#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X. *Пример:* n = 5; список 1 2 3 4 5; x = 6. Ответ 5

# import random
# n = int(input('Введите размер массива: '))
# x = int(input('Введите искомое число x: '))
# arr = []
# for i in range(n):
#     arr.append(random.randrange(n))
# print(arr)
# def nearval(arr, number):
#     return min(arr, key=lambda x: abs(number - abs(x))) 
# print(f'Ближайшее к {x} число в массиве: {nearval(arr, x)}')

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко; ● D, G – 2 очка; ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка; ● K – 5 очков; ● J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко; ● Д, К, Л, М, П, У – 2 очка; ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка; ● Ж, З, Х, Ц, Ч – 5 очков; ● Ш, Э, Ю – 8 очков; ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

letters_english = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
points_english  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   3,   3,   3,   3,   4,   4,   4,   4,   4,   5,   8,   8,   10,  10]
letters_russian = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'Д', 'К', 'Л', 'М', 'П', 'У', 'Б', 'Г', 'Ё', 'Ь', 'Я', 'Й', 'Ы', 'Ж', 'З', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Ф', 'Щ', 'Ъ']
points_russian  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   4,   4,   5,   5,   5,   5,   5,   8,   8,   8,   10,  10,  10]
letters = letters_english + letters_russian
points  = points_english  + points_russian
index = 0
sum = 0
word = input("Введите слово : ").upper()
output_word = list(word)
for char in letters:
    index += 1
    for i in range(len(output_word)):
        if output_word[i] == char:
            point_index = points[index-1]
            sum = sum + point_index
print(sum)