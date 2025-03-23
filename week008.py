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

if __name__ == '__main__':
    pass




key = 'rubiks'
#message ='Resistance is Futile But Patterns Are Infinite'
#message =iytqclrhdm sk wouqvw sou xklkysvc siy jvpaecum
#🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲🧊🔲
# A proprietary mix of Borg inevitability and Rubik’s Cube's complexity of 43 quintillion possible Rubik’s Cube states. 🧊


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
message ='Resistance is Futile But Patterns Are Infinite'
#vigenere_sq_print(vigenere_sq(alphabet))
#print(vigenere_index('r','r',alphabet))
ct = encrypt_vigenere(key, message, alphabet)
print (ct,"     <---Encrypted Message")
print (decrypt_vigenere(key, ct, alphabet), "     <-- Decrypted Message")





#print(encrypt_vigenere(key,message.lower(),alphabet))
#print(len("Resistance is Futile But Patterns Are Infinite"))
#print(len("iytqclrhdm sk wouqvw sou xklkysvc siy jvpaecum"))