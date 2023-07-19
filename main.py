import random
import math

first_number_choice = None
second_number_choice = None
digits = []
operations = ['+', '-', '*', r'/']
unique_switch = False

for i in range(6):
    while not unique_switch:
        candidate = math.floor(random.random()*25)
        if candidate not in digits:
            digits.append(candidate)
        unique_switch = True
    unique_switch = False

while first_number_choice != 'x':
    print("These are your numbers")
    print("    ".join(f'{num}' for num in digits))

    print()

    print("These are your operations")
    print("     ".join(f'{op}' for op in operations))

    print()
    print('Press "x" to quit')
    while not first_number_choice:
        try:
            first_number_choice = input("Choose a first number ")
            if first_number_choice == 'x':
                break
            first_number_choice = int(first_number_choice)
            digits.remove(first_number_choice)
        except ValueError:
            print("Number not in list")
            first_number_choice = None
            continue
    if first_number_choice == 'x':
        break

    while not second_number_choice:
        try:
            second_number_choice = input("Choose a second number ")
            if second_number_choice == 'x':
                break
            second_number_choice = int(second_number_choice)
            digits.remove(second_number_choice)
        except ValueError:
            print("Number not in list")
            second_number_choice = None
            continue
    if second_number_choice == 'x':
        break

    operation_choice = input("Choose an operation ")
    if operation_choice == 'x':
        break

    if operation_choice == '+':
        digits.append(first_number_choice + second_number_choice)
    elif operation_choice == '-':
        digits.append(first_number_choice - second_number_choice)
    elif operation_choice == '*':
        digits.append(first_number_choice * second_number_choice)
    elif operation_choice == r'/':
        digits.append(first_number_choice / second_number_choice)

    first_number_choice = None
    second_number_choice = None
