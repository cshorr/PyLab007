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
        print(f"|{'|'.join(row)}|")
        if i == 0:
            print(f'{'|-'* len(row)}|')

def letter_to_index(letter, alphabet):
    return alphabet.upper(letter.upper())
def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index].lower()

def vigenere_index(key, plaintext, alphabet):
#letter_to_index(key_letter, alphabet) % len(alphabet), alphabet))

key = "bluesmurf"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vigenere_sq_print(vigenere_sq(alphabet))
print(f"Plaintext: {plaintext}")
