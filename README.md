# Vigenère Cipher - TAKE TWO

**Last week you implemented Vigenère's cipher, but with limited knowledge of string functions, features and lists. This week we're going to revisit this cipher, but this time I want you to optimize your code by looking for areas where using lists and or any of the new string features we've learned would improve your code. I also want you to complete the BONUS decryption this time around regardless of whether you did it for extra credit last week!**

---

The Vigenère cipher is a method of encrypting text by using a keyword to alter the letters in the plaintext. The cipher uses a **Vigenère square** (a 26x26 table containing all possible alphabetic shifts) to match a keyword with the plaintext.

|   | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| B | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |
| C | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |
| D | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |
| E | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| F | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E |
| G | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F |
| H | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G |
| I | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H |
| J | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I |
| K | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J |
| L | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K |
| M | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L |
| N | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M |
| O | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N |
| P | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| Q | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |
| R | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
| S | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
| T | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S |
| U | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T |
| V | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U |
| W | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
| X | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W |
| Y | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X |
| Z | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y |

Below I show how you can encrypt a message using this square:

## 1. **Pick a Keyword and Match it to the Plaintext Sentence**

First, choose a keyword, which can be any word or phrase, and align it with the plaintext sentence you want to encrypt. If the keyword is shorter than the plaintext, repeat it until it matches the length of the sentence. 

**Example**:
- Plaintext: `THE EAGLE HAS LANDED`
- Keyword: `DAVINCI`

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 0 | 1 | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D | A | V | I | N | C | I | D | A | V | I | N | C | I | D | A | V |
| T | H | E | E | A | G | L | E | H | A | S | L | A | N | D | E | D |

## 2. **Use the Vigenère Square to Create Ciphertext**

For each letter in the plaintext, find the corresponding row in the Vigenère square for the plaintext letter, and the corresponding column for the keyword letter. The intersection of the row and column gives the encrypted (cipher) letter.

**Example**:
- Plaintext: `THE EAGLE HAS LANDED`
- Keyword: `DAVINCI`
- Ciphertext: `WHZ RCOOE PNU OAILRF`

## 3. **Derive the Ciphertext Index**

The Vigenère cipher works by shifting each letter of the **plaintext** based on the position of the corresponding **keyword letter** in the **alphabet**. Below is the mathematical explanation:

- For each letter in the plaintext, determine its index in the alphabet (A = 0, B = 1, ..., Z = 25).
- Do the same for the corresponding letter in the keyword.
- Add the two indices together and take the result modulo 26 (since there are 26 letters in the alphabet).

The resulting index gives the position of the cipher letter.

**Example**:
- Plaintext letter: `H` (index 7)
- Keyword letter: `K` (index 10)
- Cipher index: `(7 + 10) % 26 = 17` (corresponding to the letter `R`)
- You can VERIFY this with the Vigenère Square above!

Thus, `H` encrypted with `K` becomes `R`.

This process continues for each letter in the plaintext, resulting in a fully encrypted message.

# Lab Time!!!

For this lab we are going to write code to print out a Vigenère square, and write the encryption and decryption functions for a Vigenère cipher!

## Part 1 - Building a Vigenère Square

* Using the Vigenère Square in this README.md as your guide, write a function called **vigenere_sq**
    * This time around, build the square in a **list** of **list** before looping over those lists and printing the square you see below.
* As last week, use **f-strings** to print the table in a stylized way.
* Example output:
```shell
|   | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| B | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |
| C | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |
| D | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |
| E | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| F | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E |
| G | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F |
| H | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G |
| I | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H |
| J | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I |
| K | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J |
| L | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K |
| M | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L |
| N | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M |
| O | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N |
| P | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| Q | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |
| R | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
| S | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
| T | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S |
| U | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T |
| V | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U |
| W | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
| X | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W |
| Y | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X |
| Z | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y |
```

## Part 2 - Encryption

**Not much will change in this section, but review all the functions and optimize with new string features and lists where you can. One change I want you to make is to save your cipher_text in a list instead of appending to a cipher_text string. Then I want you to use `join()` to generate the return result.**

---

* Write a function `letter_to_index(letter, alphabet)` that returns the letter's `int` position in the alphabet.
* Write a function `index_to_letter(index, alphabet)` that returns the `letter` found at position `index`.
* Choose a **key** as described in the introduction, it can be any word that can be made with your **alphabet** the English alphabet in our case.
* Using the equation in the **Derive the Ciphertext Index** section write a function `vigenere_index(key_letter, plaintext_leter, alphabet)` that takes a letter from your **key** and a corresponding letter from your **plaintext** and returns the ciphertext.
    * HINT: You can use your letter_to_index function to get the index for the math!
    * HINT: You can use index_to_letter to return the cipher text!
* Finally, write a function `encrypt_vigenere(key, plaintext, alphabet)` that follows the process from the introduction to map your picked **key** to every character of your **plain text** and then uses `vigenere_index(key_letter, plaintext_letter, alphabet)` to build an encrypted string.
    * HINT: You will clearly need to loop over every letter in your plaintext.
    * HINT: You don't need to match each letter of the plain text to your key if you think **(USE % to CYCLE over the KEY letters)**
        * For example, if your key is DAVINCI, the V is at index 2, and the length is 7, so 2 % 7 would return 2, just like 9 % 7 would return 2!
            * DAVINCIDAVINCI
            * 0123456789
    * Remember, this time I want the cipher-text in a list!

## Part 3 - Decryption - NOT bonus this time

**This time this part of the lab is NOT bonus, because I want you all to have a working encryption/decryption cipher. The goal here is to recover the plain_text, but I want you to recover each plain_text character into a list and then use `join()` on the list to return the plaintext result.**

---

* In order to **decrypt** you will need to figure out how to un-rotate the cipher!
    * That means reverse `cipher_char = (key_char + plain_text_char) % len(alphabet)`
    * HINT: maybe just try: `plain_text_char = (cipher_char - key-char) % len(alphabet)`
* Write a function `undo_vigenere_index(key_letter, cypher_letter, alphabet)` that is essentially the opposite of vigenere_index. So it will return the **plain text** letter.
* Next use this function in another function `decrypt_vignere(key, cipher_text, alphabet)` to decrypt your cipher_text string completely into plain text.
    * Remember this time I want the plaintext in a list.

## Part 4 - App

* Write a for loop that gives the user a menu. 1). Encrypt, 2). Decrypt, 3). Dump Encrypted Text, 4.) Quit
    * **(I want the menu items to be in a `list()`)**
        * If you can figure it out, I'd like your menu to be a `list` of `lists` that has two elements in the inner list: 1. The menu string and 2. the function to call when that item is selected.
    * If **1). Encrypt** is selected you should prompt for plain text and store the encrypted result in a global `list` before returning to the main menu.
    * If **2). Decrypt** is selected you should loop over the global encrypted `list`, decrypt each entry, and print the text before returning to the main menu.
    * If **3). Dump Encrypted** is selected you simply print the global `list` as is!
        * HINT: Keep an eye out for redundant code, this is a good sign you can **encapsulate** it in a function and **generalize** it wih parameters.

## BONUS - (10pts)

* Invent a way to **rotate** keys for the encryption process.
    * Perhaps have another menu item that allows users to input a series of keys
    * Then, each time encrypt is selected, rotate to a new key.
        * Clearly you will have to follow the same key roatation pattern for "2). Decrypt"

## Part 5: Turn In!
[Review video of this process](https://redwoods.us-west-2.instructuremedia.com/embed/72299bfd-8420-4ad0-8af5-18fb8e32e50a)
1. **Create a GitHub Repository:**
   * Log in to your GitHub account.
   * Create a new repository with a suitable name (e.g., "python_lab6").
2. **Configure Git in PyCharm:**
   * Open the "Git" menu in PyCharm and initialize a Git repository for your project.
   * Add your GitHub remote repository by going to "Git" -> "Manage Remotes".
3. **Commit Changes:**
   * Stage all changes in your PyCharm project.
   * Commit the changes with a descriptive message (e.g., "Initial commit").
4. **Push to GitHub:**
   * Push the committed changes to your GitHub repository using the "Push" button in PyCharm.

### Submission
Submit the link from your GitHub repository containing your lab 6 repo to Canvas.
#   P y l a b 0 0 8  
 