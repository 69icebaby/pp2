#Python Generators

#Ex.1
def square_generator(n):
    for i in range(1, n + 1):
        yield i**2

n = int(input())
squares = square_generator(n)

for square in squares:
    print(square)

#Ex.2
def even_generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
even_numbers = even_generator(n)

print(*even_numbers, sep= ", ")

#Ex.3
def divisible_by_3_and_4_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
divisible_nums = divisible_by_3_and_4_generator(n)

for num in divisible_nums:
    print(num)

#Ex.4
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)

#Ex.5
def n_to_zero(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
nums = n_to_zero(n)

for num in nums:
    print(num)