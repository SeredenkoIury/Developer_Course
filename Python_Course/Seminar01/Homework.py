#====================================================
print()
print("Developer - Python_Course, Seminar_01 - homework")
print("Seredenko I.D.")
print("Full Tasks in one file.")
# Найдите сумму цифр трехзначного числа n. ===================================================================================================TASK 01

# Результат сохраните в перменную res.

# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)
# """=================================================================================================================
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
# """



# #n = 100

# # Введите ваше решение ниже
# res = n // 100 + (n // 10) % 10 + n % 10
# #print(res)


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.===========================================================TASK 02

# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
# Пример:
# n = 6 -> 1 4 1  
# n = 24 -> 4 16 4    
# n = 60 -> 10 40 10 

#===========================================
# """
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
# """

# #n = 60
# # Введите ваше решение ниже
# P = n//6
# S = P
# K = (n//6)*4
# print(P, K, S)



# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. =================================TASK 03

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# Пример:


# n = 385916 -> yes
# n = 123456 -> no

#=====================================
# """
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
# """

# n = 385916

# # Введите ваше решение ниже

# n1 = n // 100000
# n2 = (n // 10000) % 10
# n3 = (n // 1000) % 10
# n4 = (n // 100) % 10
# n5 = (n // 10) % 10
# n6 = n % 10
# if n1 + n2 + n3 == n4 +n5 +n6:
#     print("yes")
# else:
#     print("no")
# # print(n1, n2, n3, n4, n5, n6) # FOR CHECK USEING ONLY 

# Определите, можно ли от шоколадки размером a × b долек отломить c долек, ==================================================================TASK 04
# если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

# Пример:


# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no
#=============================================================================================

# """
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `a`, `b`, `c`

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `a`, `b`, `c` для проверки
# """

# # a = 3
# # b = 2
# # c = 4

# # Введите ваше решение ниже

# if c % a == 0 or c % b == 0:
#     print("yes")
# elif c > a * b:
#     print("no")
# else:
#     print("no")
