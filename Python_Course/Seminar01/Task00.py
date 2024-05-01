#====================================================
print()
print("Developer - Python_Course, Seminar_01")
print("Seredenko I.D.")
print("Full Tasks in one file.")

# print("Task 01") #================================================================================================ Task 01
# print()
# # The car ride n km per day
# # How much day the car will spend to ride the trip with m km?
# # diring the task you should not use IF or Cikles operators

# n = int(input ("Add how much kilometers the car can ride per day and press ENTER:  "))
# m = int(input("Add the Trip Distance in kilometers and press ENTER:  "))

# print("Car can ride per day ", n, " km.")
# print("The ride trip distance is  ", m, " km.")

# print("The car will spend ", (m + n - 1)//n, " days for the road")

# print("Task 02") #================================================================================================ Task 02

# # We have some different classes on the 1 class room. 
# # all of them have different numbers of people
# # and we have a desks, 1 desk - 1-2 people.
# # write the programm to know the less number desks that we need
# #a, b, c = 20, 21, 22

# a = int(input ("Add the numder of people in the first class and press ENTER:  "))
# b = int(input("Add the numder of people in the second class and press ENTER:  "))
# c = int(input ("Add the numder of people in the third class and press ENTER:  "))

# print(f" The less number of desks that we needs is {a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2}")

# print("Task 03") #================================================================================================ Task 03
# find the number of the vagons or tell than u can not do that
# tha number of the vagon starts from the locomotive in the straight way
# the person know the number of the vagon from his eyes and
# will know the number of the wagon correctly
# find the solution
# input 3 ,4 
# output 6

# a = int(input ("Add the numder of the wagon that person been chosen:  "))
# b = int(input("Add the numder of the wagon that person foundout inside:  "))
# if a == b:
#     print("There is no fast solution to find the number of the wagons in the train")
# else:
#     print("There is", b + a - 1, "wagons in the Train")

# print("Task 04") #================================================================================================ Task 04
# # Дано натуральное число, Требуется определить является ли год с данным номером високосным. 
# # если год является високосным,  то выведете YES, иначе выведете NO
# # В соответствии с григорианским календарем год является високосным если его номер кратен 4, но
# # не кратен 100, а также, если он кратен 400.

# year = int(input("add the year number to check if the year is visokosniy and press ENTER: "))

# if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
#     print("Yes, the", year, "year is visokosniy")
# else:
#     print("No,", year, "year is not visokosny")
    
# #===================== alternative decision =========================
# print("Yes, the year is visokosniy" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "No, year is not visokosny")

print("Task 05") #================================================================================================ Task 05
