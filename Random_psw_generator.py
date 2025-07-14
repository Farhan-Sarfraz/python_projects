import random
import string

print("=== Random password generator ===")

length = int(input("enter the length of password. "))
if length < 6:
    print("please enter the at least 6  characters. ")
    exit()

include_letters = input("include lettrs ? (y/n): " ).lower() == 'y'
include_symbols = input("include symbols ? (y/n): " ).lower() == 'y'
include_digits = input("include digits ? (y/n): " ).lower() == 'y'

character = ""
if include_letters:
    character += string.ascii_letters
if include_digits:
    character += string.digits
if include_symbols:
    character += string.punctuation

if character == "":
    print("you must enter at least one character. ")
    exit()
password = []

if include_letters:
    password.append(random.choice(string.ascii_letters))
if include_digits:
    password.append(random.choice(string.digits))
if include_symbols:
    password.append(random.choice(string.punctuation))
while len(password) < length:
    password.append(random.choice(character))

random.shuffle(password)

final_password = ''.join(password)
print("your oassword is : ", final_password)

