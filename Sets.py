"""
Examples

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
"""

#Ex.1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Ex.2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Ex.3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Ex.4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Ex.5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
