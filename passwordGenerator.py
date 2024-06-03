import random

print('Welcome to the Password Generator')

choice = int(input('Press 0 for custom password 1 for random password : '))

if choice == 0:
    letter = int(input("How many letters would you like : \n"))
    symbol = int(input("How many symbols would you like : \n"))
    number = int(input("How many numbers would you like : \n"))
else: 
    letter = random.randint(5,10)
    symbol = random.randint(2,5)
    number = random.randint(2,5)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = []
final_password = ''

for i in range (letter):
    password.append(random.choice(letters))

for i in range(symbol):
    password.append(random.choice(symbols))

for i in range(number):
    password.append(random.choice(numbers))

random.shuffle(password)

for i in range(len(password)):
    final_password += password[i]

print(f'Your password is : {final_password}')