# Message Cipher
# Will allow user to encrypt or decrypt a message by form or offsetting text in the alphabet.
# User will select function to encrypt or decrypt, input the message, and input the offset amount.
# Program will output encrypted or decrypted message and prompt user if they would like to use again.

import alphabet_list

def encrypt(text, shift):
    generated_text = ""
    for letter in text:
        if letter in alphabet_list.alphabet:
            letter_index = alphabet_list.alphabet.index(letter)
            new_letter_index = letter_index + shift
            new_letter = alphabet_list.alphabet[new_letter_index]
            generated_text += new_letter
        else: 
            generated_text += letter
    print(f"Here is the ecoded result:\n{generated_text}")

def decrypt(text, shift):
    generated_text = ""
    for letter in text:
        if letter in alphabet_list.alphabet:
            letter_index = alphabet_list.alphabet.index(letter)
            new_letter_index = letter_index - shift
            new_letter = alphabet_list.alphabet[new_letter_index]
            generated_text += new_letter
        else: 
            generated_text += letter
    print(f"Here is the decoded result:\n{generated_text}")

print("Welcome to Message Cipher.")

# While loop added to keep program running if user wants after initial message generated

keep_running = "yes"
while keep_running == "yes":

    encrypt_or_decrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message.\n").lower()
    shift_input = int(input("Shift amount:\n"))

    if encrypt_or_decrypt == "encode":
        encrypt(text_input, shift_input)
    else:
        decrypt(text_input, shift_input)

    keep_running = input("Type 'yes' to run again, otherwise type 'no':\n")