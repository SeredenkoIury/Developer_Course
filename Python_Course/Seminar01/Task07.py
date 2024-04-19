a = 5
while a > 0:
    print(a)
    if a == 3:
        break
    a -= 1
else:
    print("FULL STOP WITHOUT BREAK")
    
my_str = "abrakadabra"
for elem in my_str:
    print(elem, end = " ")
    

print(" ")
print("============== or ================")

i = 0
while i < len(my_str):
    print(my_str[i], end = " ")
    i += 1
