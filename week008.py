import psutil
import os
from sys import exit



def vigenere_head(alphabet):
    return list(' ') + list(alphabet)

def vigenere_sq(alphabet):
    alphabet = list(alphabet)
    sq_list = [vigenere_head(alphabet)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            print(f'{"|---"* len(row)}|')

def letter_to_index(letter, alphabet):
    return alphabet.find(letter)

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return index_to_letter(
        (letter_to_index(plaintext_letter,alphabet) +
         letter_to_index(key_letter,alphabet)) % len(alphabet), alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cypher_text = []
    counter = 0
    for i in plaintext:
        if i == ' ':
            cypher_text.append(' ')
        elif i in alphabet:
            cypher_text.append (vigenere_index(key[counter % len(key)],i, alphabet))

            counter += 1
    return ''.join(cypher_text)

def non_vigenere_index(key_letter, cypher_text, alphabet):
    return index_to_letter(
        (letter_to_index(cypher_text,alphabet) -
         letter_to_index(key_letter,alphabet)) % len(alphabet), alphabet)

def decrypt_vigenere(key, cypher_text, alphabet):
    plain_text = []
    counter = 0
    for i in cypher_text:
        if i == ' ':
            plain_text.append(' ')
        elif i in alphabet:
            plain_text.append (non_vigenere_index(key[counter % len(key)], i, alphabet))
            counter += 1
    return ''.join(plain_text)

def enc_menu(key, alphabet, encrypted_list):
    plaintext = input("Enter the text you'd like to encrypt: ")
    encrypted_list.append(encrypt_vigenere(key, plaintext, alphabet))

def dec_menu(key, alphabet, encrypted_list):
    for cypher_text in encrypted_list:
        print (cypher_text)

    cypher_text = input("Enter the text you'd like to decrypt: ")

    return decrypt_vigenere(key, cypher_text, alphabet)

def dec_dump_menu(encrypted_list):
    for cypher_text in encrypted_list:
        print(cypher_text)
def main():
    key = 'rubiks'
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    message ='Resistance is Futile But Patterns Are Infinite'
    encrypted_list = []
    menu = [
        ['1). Encrypt',enc_menu, [key, alphabet, encrypted_list]],
        ['2). Decrypt', dec_menu, [key, alphabet, encrypted_list]],
        ['3). Dump Decrypt', dec_dump_menu, [encrypted_list]],
        ['4). Quit', exit, [0]]
    ]
    while True:
        print ("_"*188)
        for menu_item in menu:
            print(menu_item[0])
        try:
            choice = int (input ("Make your choice: "))
            if not (0 < choice  <= len(menu)):
                print("././././././...YOU HAVE MADE A GRAVE ERROR ----Invalid choice")
            else:
                menu[choice -1][1](*menu[choice -1][2])
        except ValueError as Ignored:
                print("./././././.ERROR ALERT!!!Invalid choice, Enter an (INT) number betwixt 1 and 4 ")
        encrypted_list.append(menu[1][1](*menu[1][2]))
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, "MB")
    #for _ in range(2):
        #menu[0][1](*menu[0][2])
        #)

    #menu[1][1](*menu[1][2])
    #menu[2][1](*menu[2][2])
    #menu[3][1](*menu[3][2])
if __name__ == '__main__':
            main()

    #vigenere_sq_print(vigenere_sq(alphabet))
    #print(vigenere_index('r','r',alphabet))
    #ct = encrypt_vigenere(key, message, alphabet)
    #print (ct,"     <---Encrypted Message")
    #print (decrypt_vigenere(key, ct, alphabet), "     <-- Decrypted Message")
#print(encrypt_vigenere(key,message.lower(),alphabet))
#print(len("Resistance is Futile But Patterns Are Infinite"))
#print(len("iytqclrhdm sk wouqvw sou xklkysvc siy jvpaecum"))
#🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲

