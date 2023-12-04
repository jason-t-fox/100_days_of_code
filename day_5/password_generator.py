import random

#variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_builder = []
final_password = ""
counter = 0

letter_input_error = "please choose a number."
number_input_error = "Please choose a number greater then zero."

#run program!
#gather and sanitize inputs
print("Welcome to the PyPassword Generator!\n")
try:
    number_letters = int(input("How many letters would you like in your password?\n"))
except:
    print(letter_input_error)
    exit()
finally:
    pass

if number_letters < 1:
    print(number_input_error)
    exit()

try:
    number_symbols = int(input(f"How many symbols would you like?\n"))
except:
    print(letter_input_error)
    exit()
finally:
    pass

if number_symbols < 1:
    print(number_input_error)
    exit()

try:
    number_numbers = int(input(f"How many numbers would you like?\n"))
except:
    print(letter_input_error)
    exit()
finally:
    pass

if number_numbers < 1:
    print(number_input_error)
    exit()

#begin building the password
#while loop example
counter = 0
while counter < number_letters:
    password_builder.append(random.choice(letters))
    counter += 1

#for loop example
for item in range(1, number_symbols + 1):
    password_builder.append(random.choice(symbols))

# using random choices makes a loop unnecessary (this lesson was focused on building loops specifically, but I wanted to show this option as well.)
password_builder += random.choices(numbers, k=number_numbers)

random.shuffle(password_builder)

final_password = "".join(password_builder)
print(f"\nYour final password is:\n\n{final_password}")

