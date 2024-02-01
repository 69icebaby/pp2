"""
Examples:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""
#Ex.1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Ex.2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Ex.3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Ex.4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Ex.5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Ex.6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Ex.7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Ex.8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))