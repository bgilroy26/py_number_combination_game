import random
import math
import itertools
import collections

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
    save = numbers.copy()
    # generate the number of numbers that you will use (at least 3)
    numbers_used = math.floor(random.random()*3)+3
    operations_used = numbers_used - 1

    pre_target_numbers = random.choices(digits, k=numbers_used)
    pre_target_operations = random.choices(operations, k=operations_used)

    combo = itertools.zip_longest(pre_target_numbers, pre_target_operations)

    # remove None from tail
    combo.pop()

    # flatten combo and return list of numbers and operations
    return ([item for sublist in combo for item in sublist], numbers)



# expr is the numbers and operations from create_target
def evaluate_target(expr_pair):
    expr = expr_pair[0]
    save = expr_pair[1]

    len_switch = True
    in_list_switch = True
    positive_switch = True
    integer_switch = True
    abs_switch = True
    while len_switch or in_list_switch or positive_switch \
            or integer_switch or abs_switch:
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
            if expr[0] not in save:
                in_list_switch = False
            else:
                return evaluate_target(create_target(save))
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


    return int(expr[0])

def play(nums, goal):
    print()
    print("##############################################")
    print("##### WELCOME TO NUMBER COMBINATION GAME #####")
    print("##############################################")
    print()
    first_number_choice = None
    second_number_choice = None
    operation_choice = None
    starter_nums = nums.copy()

    while True:
        print(f"This is your target: {goal}")
        print()
        print("These are your numbers")
        print("    ".join(f'{num}' for num in nums))

        print()

        print("These are your operations")
        print("     ".join(f'{op}' for op in operations))

        print()
        print('Press "r" to restart')
        print('Press "x" to quit')

        while not first_number_choice:
            first_number_choice = input("Choose a first number ")
            if first_number_choice == 'x':
                break
            if first_number_choice == 'r':
                break
            first_number_choice = int(first_number_choice)
            try:
                nums.remove(first_number_choice)
            except ValueError:
                print("Number not in list")
                first_number_choice = None
                continue
        if first_number_choice == 'x':
            return None
        if first_number_choice == 'r':
            return play(starter_nums, goal)

        while not operation_choice:
            operation_choice = input("Choose an operation ")
            if operation_choice == 'x':
                return None
            if operation_choice == 'r':
                return play(starter_nums, goal)
            if operation_choice not in ['+', '-', '*', r'/']:
                operation_choice = None
                continue


        while not second_number_choice:
            second_number_choice = input("Choose a second number ")
            # test for divisibility
            if operation_choice == r'/' and \
                    int(second_number_choice) % int(first_number_choice) != 0:
                print("Divisor must divide evenly")
                second_number_choice = None
                continue
            # test that subtraction result is >= 1
            if operation_choice == '-' and \
                    int(second_number_choice) >= int(first_number_choice):
                print("Second term in subtraction must be less than first term")
                second_number_choice = None
                continue
            if second_number_choice == 'x':
                break
            if second_number_choice == 'r':
                break
            second_number_choice = int(second_number_choice)
            try:
                nums.remove(second_number_choice)
            except ValueError:
                print("Number not in list")
                second_number_choice = None
                continue
        if second_number_choice == 'x':
            return None
        if second_number_choice == 'r':
            return play(starter_nums, goal)

        new_value = evaluate_expression(first_number_choice,
                                        second_number_choice,
                                        operation_choice
                                        )

        if new_value == goal:
            print("YOU WIN, YOU MARVELOUS DEVIL!")
            break
        else:
            nums.append(new_value)

        first_number_choice = None
        operation_choice = None
        second_number_choice = None

##############
# BEGIN GAME #
##############

# Create 6 unique numbers between 1 and 25 inclusive
digits = [math.floor(random.random()*24 + 1) for _ in range(6)]
while len(digits) != len(set(digits)):
    dupes = [item for item, count in collections.Counter(digits).items()
             if count > 1]
    retries = len(dupes)
    for dupe in dupes:
        digits.remove(dupe)
    digits.extend(math.floor(random.random()*24 + 1) for _ in range(retries))

target = evaluate_target(create_target(digits))

play(digits, target)
