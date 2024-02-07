"""Examples
def my_function():
  print("Hello from a function")

  def my_function():
  print("Hello from a function")


my_function()

def my_function(fname):
  print(fname + " Refsnes")

  
my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
"""

#Ex.1
def my_function():
  print("Hello from a function")

#Ex.2
def my_function():
  print("Hello from a function")

my_function()

#Ex.3
def my_function(fname, lname):
  print(fname)

#Ex.4
def my_function(x):
  return x + 5

#Ex.5
def my_function(*kids):
  print("The youngest child is " + kids[2])

#Ex.6
def my_function(**kid):
  print("His last name is " + kid["lname"])
  
