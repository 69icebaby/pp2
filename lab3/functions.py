#Ex.1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
    
grams_value = int(input())
result = grams_to_ounces(grams_value)
print(result)

#Ex.2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit_temperature = float(input("Enter Fahrenheit temperature: "))

celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")

#Ex.3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None, None 

numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)

if chickens is not None and rabbits is not None:
    print(f"There are {chickens} chickens and {rabbits} rabbits.")
else:
    print("No solution found.")

#Ex.4
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in user_input.split()]

prime_numbers = filter_prime(numbers_list)

print(f"Original list: {numbers_list}")
print(f"Prime numbers: {prime_numbers}")

#Ex.5
from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)

    for perm in perms:
        print(''.join(perm))

user_input = input("Enter a string: ")

print_permutations(user_input)


#Ex.6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

user_input = input("Enter a sentence: ")

result = reverse_words(user_input)

print("Reversed Words:", result)

#Ex.7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input("Enter a list of integers separated by spaces: ")
nums_list = [int(num) for num in user_input.split()]

result = has_33(nums_list)

print("List:", nums_list)
print("Contains 3 next to 3:", result)

#Ex.8
def spy_game(nums):
    spy_sequence = [0, 0, 7]
    index = 0

    for num in nums:
        if num == spy_sequence[index]:
            index += 1
            if index == len(spy_sequence):
                return True

    return False

user_input = input("Enter a list of integers separated by spaces: ")
nums_list = [int(num) for num in user_input.split()]

result = spy_game(nums_list)

print("List:", nums_list)
print("Contains the spy sequence:", result)

#EX.9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius)

print(f"The volume of the sphere with radius {radius} is: {result:.2f}")

#Ex.10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

user_input = input("Enter a list of elements separated by spaces: ")
original_list = [int(num) for num in user_input.split()]

result = unique_elements(original_list)

print("Original list:", original_list)
print("List with unique elements:", result)

#Ex.11
def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_s == cleaned_s[::-1]

input_phrase = input("Enter a word or phrase: ")
result = is_palindrome(input_phrase)

if result:
    print(f"{input_phrase} is a palindrome.")
else:
    print(f"{input_phrase} is not a palindrome.")


#Ex.12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

user_input = input("Enter a list of integers separated by spaces: ")
numbers_list = [int(num) for num in user_input.split()]

histogram(numbers_list)

#Ex.13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()

#Ex.14
# my_functions.py

import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

def histogram(numbers):
    for i in range(max(numbers), 0, -1):
        line = ''.join('*' if num >= i else ' ' for num in numbers)
        print(line)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
