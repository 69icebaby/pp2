"""
Examples

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
"""
#Ex.1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Ex.2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Ex.3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Ex.4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])