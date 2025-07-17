
import random
import string

alphabet = string.ascii_letters
shift = input("how much you want shift(e.g 3 or 5 ) ??")
dirction = input("type 'encode' for encrypt, type 'decode' for decrypt. ")
message = input("type shift message. ").lower()

def encode(plain_message , plain_shift):
    cipher_text = ""
    for letter in plain_message:
        position = alphabet.index(letter)
        new_position = position + int(plain_shift)
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"encode message is {cipher_text}")
# second function for decode
def decode(plain_message , plain_shift):
    cipher_text = ""
    for letter in plain_message:
        position = alphabet.index(letter)
        new_position = position - int(plain_shift)
        cipher_text += alphabet[new_position]
    print(f"decode message is {cipher_text}")

if dirction == "encode":
    encode(message, shift)
elif dirction == "decode":
    decode(message, shift)







