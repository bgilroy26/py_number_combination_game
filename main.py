import random
import math
import itertools

first_number_choice = None
second_number_choice = None
digits = []
operations = ['+', '-', '*', r'/']
unique_switch = False


def evaluate_expression(first, second, op):

    output = None

    if op == '+':
        output = first + second
    elif op == '-':
        output = first - second
    elif op == '*':
        output = first * second
    elif op == r'/':
        output = first / second

    return output


# numbers is a list of 6 numbers that we
# have at the beginning of the game
def create_target(numbers):
    save = numbers
    # generate the number of numbers that you will use (at least 3)
    numbers_used = math.floor(random.random()*3)+3
    operations_used = numbers_used - 1

    pre_target_numbers = random.choices(digits, k=numbers_used)
    pre_target_operations = random.choices(operations, k=operations_used)

    combo = itertools.zip_longest(pre_target_numbers, pre_target_operations)

    # flatten combo and return list of numbers and operations
    return ([item for sublist in combo for item in sublist], numbers)



#expr is the numbers and operations from create_target
def evaluate_target(expr_pair):
    expr = expr_pair[0]
    save = expr_pair[1]
    # remove None from tail
    expr.pop()

    len_switch = True
    positive_switch = True
    integer_switch = True
    abs_switch = True
    while len_switch or positive_switch or integer_switch or abs_switch:
        first_number = expr.pop()
        operation = expr.pop()
        second_number = expr.pop()
        expr.append(evaluate_expression(first_number,
                                        second_number,
                                        operation
                                        )
                    )

        if len(expr) == 1:
            len_switch = False
        if not len_switch:
            if expr[0] < 400:
                abs_switch = False
            else:
                return evaluate_target(create_target(save))
        if not abs_switch:
            if expr[0] > 0:
                positive_switch = False
            else:
                return evaluate_target(create_target(save))
        if not positive_switch:
            if expr[0] == int(expr[0]):
                integer_switch = False
            else:
                return evaluate_target(create_target(save))

    return expr

##############
# BEGIN GAME #
##############
for _ in range(6):
    while not unique_switch:
        candidate = math.floor(random.random()*25)
        if candidate not in digits:
            digits.append(candidate)
        unique_switch = True
    unique_switch = False

target = evaluate_target(create_target(digits))

while first_number_choice != 'x':
    print(f"This is your target: {target}")
    print()
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

    new_value = evaluate_expression(first_number_choice,
                                      second_number_choice,
                                      operation_choice
                                      )

    if new_value == target:
        print("YOU WIN, YOU MARVELOUS DEVIL!")
        break
    else:
        digits.append(new_value)

    first_number_choice = None
    second_number_choice = None
