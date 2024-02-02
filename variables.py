"""
Examples

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))
"""
#Ex.1
carname = "Volvo"

#Ex.2
x = 50

#Ex.3
x = 5
y = 10
print(x + y)

#Ex.4
x = 5
y = 10
z = x + y
print(z)

#Ex.5
x, y, z = "Orange", "Banana", "Cherry"

#Ex.6
x = y = z = "Orange"

#Ex.7
def myfunc():
  global x
  x = "fantastic"