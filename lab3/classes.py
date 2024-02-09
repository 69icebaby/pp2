#Ex.1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

if __name__ == "__main__":
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()

#Ex.2
class Shape:
    def __init__(self):
        pass

    def area(self):
         return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
         return self.length ** 2

if __name__ == "__main__":
    shape = Shape()
    print("Area Shape:", shape.area())

    length_of_square = float(input("Use the side length of the square: "))
    
    square = Square(length_of_square)
    print("Square area:", square.area())

#Ex.3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    length_of_rectangle = float(input("Enter the length of the rectangle: "))
    width_of_rectangle = float(input("Enter the width of the rectangle: "))

    rectangle = Rectangle(length_of_rectangle, width_of_rectangle)
    
    print("Area of the rectangle:", rectangle.area())

#Ex.4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

if __name__ == "__main__":
    x1 = float(input("Enter x-coordinate for the first point: "))
    y1 = float(input("Enter y-coordinate for the first point: "))
    
    point1 = Point(x1, y1)

    point1.show()

    x2 = float(input("Enter x-coordinate for the second point: "))
    y2 = float(input("Enter y-coordinate for the second point: "))
    
    point2 = Point(x2, y2)

    point2.show()

    distance = point1.dist(point2)
    print(f"Distance between the two points: {distance}")

#Ex.5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

if __name__ == "__main__":
    account_owner = input("Enter the account owner's name: ")
    account = BankAccount(owner=account_owner)

    account.deposit(1000)
    account.withdraw(500)
    account.deposit(200)
    account.withdraw(1000)  

    print(f"Final balance for {account.owner}: ${account.balance}")

#Ex.6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    
    numbers = list(map(int, input_numbers.split()))

    prime_numbers = list(filter(lambda x: is_prime(x), numbers))

    print("Original list:", numbers)
    print("Prime numbers:", prime_numbers)


