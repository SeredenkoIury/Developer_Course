#==================================Lection Python 01 Task1 
"""
Задача №1. Решение в группах
Семинар 1. Ввод-вывод, операторы ветвления
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.

Input:
n = 700
m = 750
Output:
2
"""
from math import ceil

m, n = 1400, 700 
#print(ceil(m / n)) # решение через готовую функцию
print((m + n - 1) //n) # решение через собственное решение


