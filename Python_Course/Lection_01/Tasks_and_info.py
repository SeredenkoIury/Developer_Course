print()
print("Developer - Python_Course, Lection_01")
print("Seredenko I.D.")

# print() #=============================================================================================== Info
# # для запуска кода - нажать на стрелочку в правом верхнем углу, или Ctrl + F + 5
# # для запуска кода с терминала нужно в терминале напечатать - python Tasks_And_info.py
# # то есть написать пайтон и название файла который хотим запустить

# print(5) # command will writ the number 5
# print(5, 8, 6) # command will write 5 8 4


# print() #==================================================================================================== Typisation

# # Python have the dynapik typisation. than means that we shouldnt write int, str, bool and ect.
# # For example

# n = 6
# n1 = None
# n2 = 6.89

# print(n)
# print(n1)
# print(n2)

# print() #==================================================================================================== Words to print
# to make a string u should use '' or ""
# For example

# n3 = 'hey, hi'
# n4 = "Hello!"
# print(n3)
# print(n4)

# print() #==================================================================================================== Types
# # to find out the type of our n5, we should tape print(type n5)
# # this commant will write the type of n5
# # For example
# n5 = 26
# print(type(n5))
# n6 = 'a string probably'
# print(type(n6))

# print() #==================================================================================================== "" symb inside
# # if we need "" sybmols inside of our string, we should use two different types of the symbols
# # you can also use the \ symbol before " or ' to use them
# # for example

# n7 = 'The name of this book is "Book", interesting, yeah?'
# print(n7)
# n8 = "The name of this book is 'Book', interesting, yeah?"
# print(n8)
# n9 = "The name of this book is \"Book\", interesting, yeah?"
# print(n9)
# n10 = 'The name of this book is \'Book\', interesting, yeah?'
# print(n10)

# print() #==================================================================================================== Comments
# # as far as u can see you can use the # symbol to comment
# # you can also use """ before and """ after
# # the third variant to comment is to have all strings to cimment and press Ctrl + k and after Ctrl + C
# # for the third variant to uncomment you should use Ctrl + K and after Ctrl + U
# # for example

# #print(type(n5))n5 = 26

# """
# print(type(n5))n5 = 26
# print(type(n5))n5 = 26
# """

# # print(type(n5))n5 = 243
# # print(type(n5))n5 = 262

# print() #==================================================================================================== Interpolation
# # It is the method to type lots of things with different types in one print
# # use the , symbol between to write without any simbols between
# # use the '' or "" to write something between
# # use the f" " to write all inside and use the {} sybmols with data of the a/b/c
# # use the "".format() to write faster and use everything you want between {}
# # For example

# a = 5
# b = 5.93
# c = 'The Interpolation'

# print(a, b, c)

# print(a, '-', b, '-', c) 

# print(f"{a} - {b} - {c}") 

# print("{} - {} - {}".format(a, b, c))

# print("{} well {} thats great {}".format(a, b, c))

# print() #==================================================================================================== Adding Data from the console
# # for add the data from the console use input()
# # u should also make the storage for the data in 1 string
# # you can use all types of data in case of dynamic typisation
# # use the input('') with some message inside the '' to type the add message in one string withiut print() fnc
# # for example

# print("Add the Data for a and Press ENTER: ")
# a = input()
# print("Your Data for \"a\" is", a)


# b = input('Add Another Data for /"b/" and Press ENTER: ')
# print("Your Data for \"b\" is", b)

# print() #==================================================================================================== The type translarion
# # To translate the type u should write the type
# # For example
# #======================= To Int
# c = 5.89
# print(c)
# print(type(c))

# c = int(c)
# (printc)
# print(type(c))

# #======================= To String
# c = 5.89
# print(c)
# print(type(c))

# c = str(c)
# print(c + '6-maybeline')
# print(type(c))

# #======================= To bool
# c = 1
# print(c)
# print(type(c))

# c = bool(c)
# print(c)
# print(type(c))

# #======================= We can not - errors
# c = 'Oh, noo, this is ERROR'
# print(c)
# print(type(c))

# c = int(c)
# print(c)
# print(type(c))

# print() #==================================================================================================== The sum of 2 numbers
# # Write the programm than will summ 2 numbers from the console
# # To do that, we should translate string type to int. we can do that inside of the input string
# # in the case of inside of the string remember to use ()

# print("Add the Data for a and Press ENTER: ")
# a = int (input())
# b = int (input('Add Another Data for /"b/" and Press ENTER: '))
# print(a, ' + ', b, ' = ', a + b) # if a = 5 and b = 7 this print will write 57 

# print() #==================================================================================================== main operations
# +  is the plus operation
# - is the minus operation
# * is the multiply operation
# / is the full cutting operation 4 / 2 = 2, 5 / 2 = 2.5 
# % is the persent operation 5 % 2 = 5, (cause 5:2=2,5 and the lasts is 5)
# // is the cutting operation without lasts 4,5 // 2 = 2,  5 // 2 = 2 (cause 4,5:2=2,25 and 5:2=2,5 ; in both int is 2) 
# ** is the multiply highly  2**4 = 2*2*2*2 = 16

# print() #==================================================================================================== operations priority
# 1st priority is **
# 2nd priority is *
# 3rd priority is /
# 4th priority is //
# 5th priority is %
# 6th priority is +
# 7th priority is -

# print() #==================================================================================================== smart cut numbers (2,87777 = 2)
# use round(b, 3) where b is the numbers, 3 is the number of symbols after type
# a = 5.7777483
# b = 6.6643423
# print(a * b)
# print(round(a * b, 3))

# print() #==================================================================================================== Smart++
# iter = 243
# print(iter)
# iter += 3 # iter = iter + 3
# print(iter)
# iter -= 4 # iter = iter - 4
# print(iter)
# iter *= 5 # iter = iter * 5
# print(iter)
# iter /= 5 # iter = iter / 5
# print(iter)
# iter //= 5 # iter = iter // 5
# print(iter)
# iter %= 5 # iter = iter % 5
# print(iter)
# iter **= 5 # iter = iter ** 5
# print(iter)

# print() #==================================================================================================== Logical Operations
#   >    is more
#   >=   is more or equal
#   <    is less
#   <=   is less or equal
#   ==   is equal
#   !=   is not equal
#   not  is if womething is not
#   and  is something and something
#   or   is omething or something

# a = 1 > 4           # false
# print(a)
# a = 1 < 4 and 5 > 2 # true
# print(a)
# a = 1 == 2          # false
# print(a)
# a = 1 != 2          # true
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)       # true
# a = 1 < 3 < 3 < 10
# print(a)            # true

# print() #==================================================================================================== If, If-Else
# if condition:
#     operator
#     operator
# else:
#     operator
      
# if condition1:
#     operator
#     operator
# elif condition2:
#     operator
#     operator
# else:
#     operator

# if condition1 and condition2:      both of them
#     operator
    
# if condition1 or condition2:       one of them
#     operator

# ====================================================================================== IF ELSE ELIF Program Example
# username = input('Please add Your Name and press ENTER: ')
# if username == 'Iury' or username == 'Yury' or username == 'Yiry' or username == 'Yuri':
#     print('Hi men, really glad to meet You))')
# elif username == 'Max' or username == 'Maxim' or username == 'Maximka':
#     print('Hi Max, Dude i waited for see you right here')
# elif username == 'Barbara' or username == 'Betty' or username == 'Rafael' or username == 'Raf':
#     print ('Hello my darling! you have such a beautifull name honey!')
# else:
#     print('Hello, ', username )
    
# print() #==================================================================================================== While

# while condition:
#     operator 1
#     operator 2

# ========================================================================================= WHILE code program example
# # Summ of the numbers symbols
# n = int(input('Add the number and press enter: '))
# summ = 0
# while n > 0:
#     x = n % 10
#     summ = summ + x
#     n = n // 10

# print (summ)

# print() #=================================================================================================== While-Else

# while condition:
#     operator 1
#     operator 2
# else:              //WORKS ONLY WITH BREAK
#    operator 1
#    operator 2

# ========================================================================================== WHILE-ELSE code program example

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print("EMERGENCY BREAK STOP")
#     print('works with break command only')
# print(i)

#  ============================================================ alternative break with the flag, finding the lowest cut number
# finding the lowest cut number

# n = int(input('Add the number to find the lowest cut number: '))
# flag = True
# i = 2
# while flag:            ## while flag == true
#     if n % i == 0:
#         flag = False
#         print(i, ' is the lower cun number of the ', n)
#     elif i > n // 2:
#         print (n, ' have no cut number between 1 and inself')
#         flag = False
#     i += 1
# ========================================================================================== for & range
## последовательность и цикл фор
# for i in enumeration:
#     operator1
#     operator2
# ============================================

# for i in 1, -2, 14, 5:
#     print(i)
# result::: 1 -2 3 15 5

# =============================================

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # -------
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20)
# for i in r:
#     print(i)
# #will print 100 80 60 40 20

# =============================================

# a = 'querty'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print()
# ============================
# b = 'querty'
# for i in b:
#     print(i)
    
# for z in 'qazwsxedc':
#     print(z)
# ============================
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
# ========================================================================================== STRINGS
# text = 'СъЕШЬ еще этих МяГкИх французких булок'
# print(text)
# print(len(text)) # Show us the string size
# print('еще' in text) # show us does the string have this word or ect (true or false)
# print(text.replace('еще','ЕЩЕ')) #changeing the text
# print(text.lower()) #all symbols down
# print(text.upper()) #all symbols CAPS

#=====================================

text = 'СъЕШЬ ещё этих МяГкИх французких булок'
text = text.lower()
# print(text)                     #съешь еще этих мягких французких булок
# print(text[0])                  #с
# print(text[1])                  #ъ
# print(text[len(text)-1])        #к
# print(text[-1])                 #k
# print(text[-5])                 #б
# print(text[ : ])                #съешь еще этих мягких французких булок //everything
# print(text[ :2])                #съ // from 0 to 2 elements - 1 element
# print(text[20:])                # from 20th element to the end
# print(text[:20])                # from start to the 20th element
# print(text[0:len(text):6])      #from the 0th to the end with step of 6
# print(text[0:len(text):-2])     #ок from the start to the end with start from last 2
# print(text[2:9])                #ешь еще // fron the 2 to the 9 element without 9
# print(text[6:-18])              # // from the 6th to the 18th from the end
# print(text[::6])                #ок from the 0th to rhe end with step of 6


text = text[2:9] + text[-5] + text[:2]
print(text)



