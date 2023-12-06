import art

# Set up Functions (this could be a class for better code organization)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(art.logo)
def calculator():
    operations = {"+": add, "-": subtract, "/": divide, "*": multiply}
    continue_calculating = True
    num1 = float(input("What's the first number? ")) #input first number
    for value in operations:
        print(value)

    while continue_calculating == True: # begin loop to keep operating on the total as long as the user wishes to
        operation_symbol = input("Pick an operation from the options above: ") # input operation
        num2 = float(input("What's the next number? ")) # input next number
        calc = operations[operation_symbol]
        calc_result = calc(num1, num2) #use function from the operations dict
        print(f"{num1} {operation_symbol} {num2} = {calc_result}")
        continue_calculating_choice = input(f"Type 'y' to continue calculating with {calc_result}, 'n' to exit, 's' to start a new calculation: ").lower()
        if continue_calculating_choice == 'y': 
            num1 = calc_result
        elif continue_calculating_choice == 's': # start a new calculation
            continue_calculating = False
            calculator()
        elif continue_calculating_choice == 'n':
            print("Done!")
            continue_calculating = False
        else:
            print("Invalid choice, ending program")
            continue_calculating = False


#begin program
calculator()