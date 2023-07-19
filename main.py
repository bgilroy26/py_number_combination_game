import random
import math

digits = []
operations = ['+', '-', '*', r'/']

for i in range(6):
    digits.append(math.floor(random.random()*25))

print("These are your numbers")
print("    ".join(f'{num}' for num in digits))

print()

print("These are your operations")
print("     ".join(f'{op}' for op in operations))

first_number_choice = input("Choose a first number ")
second_number_choice = input("Choose a second number ")

operation_choice = input("Choose an operation ")

