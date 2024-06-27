
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Tech Password Generator!")
nr_letters = int(input("Please enter the desired length for your password\n"))
nr_symbols = input(f"Do you want symbols in your password?\n")
nr_numbers = input(f"Do you want Numbers in your password?\n")


password_list = letters


if nr_symbols.lower() == 'yes':

    password_list.append(symbols)

if  nr_numbers.lower() == 'yes':
    password_list.append(numbers)






random.shuffle(password_list)

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(password_list)

print(f"Your password is: {password}")
# for char in password_list:
#   password += char

