#Python Math Library

#Ex.1
import math

def radian(n):
    p = math.pi
    formula = n * (p / 180)
    print(formula)

n = int(input())
radian(n)

#Ex.2
def trapezoid(h, b1, b2):
    area_trapezoid = ((b1 + b2)/2) * h
    print(area_trapezoid)

h, b1, b2 = int(input()), int(input()), int(input())
trapezoid(h, b1, b2)

#Ex.3
def regular_polygon(num_sides, length_side):
    area = (num_sides * length_side ** 2) / (4 * math.tan(math.pi / num_sides))
    print(math.trunc(area))

num_sides, length_side = int(input()), int(input())
regular_polygon(num_sides, length_side)

#Ex.4
def area_of_parallelogram(l, h):
    formula = l * h
    print(formula)

l, h = float(input()), float(input())
area_of_parallelogram(l, h)