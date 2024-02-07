"""
Examples

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass
  
x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
"""

#Ex.1
class Student(Person):

#Ex.2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()