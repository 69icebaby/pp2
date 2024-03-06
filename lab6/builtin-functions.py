#Python Builtin-functions

#Ex.1
import time
import math

nums = input().split()
some_list = [int(num) for num in nums]
def pr(l):
    p = 1
    for i in l:
        p = eval("p*i")
    return p
print("product:", pr(some_list))

#Ex.2
mystr = input()
def c(s): 
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for k in s if k.islower())
    return upper, lower
u, l = c(mystr)
print("Uc num:", u, "\nLC num:", l)

#Ex.3
n = input()
def p(s1):
    s2 = s1[::-1]
    if s1 == s2:
        print("palindrome")
    else:
        print("not palindrome")
p(n)

#Ex.4
num = int(input("enter num: "))
ms = int(input("enter ms: "))
s = ms / 1000
time.sleep(s)

print(math.sqrt(num))

#Ex.5
mytuple = tuple(input())
def my_func(t):
    return all(t)
print(my_func(mytuple))