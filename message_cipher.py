# Message Cipher
# Will allow user to encrypt or decrypt a message by form or offsetting text in the alphabet.
# User will select function to encrypt or decrypt, input the message, and input the offset amount.
# Program will output encrypted or decrypted message and prompt user if they would like to use again.

from alphabet_list import alphabet
from ascii_art import intro_art

def cipher(text, shift):
    generated_text = ""
    if encrypt_or_decrypt == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index + shift
            new_letter = alphabet[new_letter_index]
            generated_text += new_letter
        else: 
            generated_text += letter
    print(f"Here is the {encrypt_or_decrypt}d result:\n{generated_text}")

print(intro_art)

# While loop added to keep program running if user wants after initial message generated

keep_running = True
while keep_running:

    encrypt_or_decrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message.\n").lower()
    shift_input = int(input("Shift amount:\n")) % 26

    cipher(text_input, shift_input)

    run_again = input("Type 'yes' to run again, otherwise type 'no':\n")
    if run_again == "no":
        keep_running = False
        print("Goodbye")
    