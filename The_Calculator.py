### The Calculator Project
from art import logo

# 1. Write all four functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# 2. Add all functions into a dictionary as the values. Keys = "+", "-", "*". "/"
calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# 3. Use the dictionary operations to perform the calculations
n1 = 4
n2 = 8
print(calc_operations["*"](4, 8))

def calculator():
    print(logo)

    num_1 = float(input("Enter the first number: "))
    run = True
    while run:
        for c in calc_operations:
            print(c)
        perform = input("Type a math operation: ")
        num_2 = float(input("Enter the second number: "))

        calculation = calc_operations[perform]
        result = calculation(num_1, num_2)

        print(f"{num_1} {perform} {num_2} = {result}")

        print(f"Type 'y' to continue calculation with {result}, type 'n' to quit or type 'new' for new calculation")
        continue_calc = input("Type y/n/new: ")
        if continue_calc == 'y':
            run = True
            num_1 = result
        elif continue_calc == 'n':
            run = False
            print("Thank you for using this calculator")
        elif continue_calc == 'new':
            calculator()
        else:
            print("Your input is invalid")
            run = False
            print("Thank you for using this calculator")

calculator()
