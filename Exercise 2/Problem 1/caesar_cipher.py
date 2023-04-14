## Caesar Cipher

import string
alphabet = list(string.ascii_uppercase)

key = 9
plaintext = "Hello"
ciphertext = ""

for letter in plaintext.upper():
    pt_index = alphabet.index(letter)
    ct_index = (pt_index + key) % 26
    ciphertext+=alphabet[ct_index]
    
print("Plain Text = ", plaintext.upper())
print("Cipher Text = ", ciphertext)
    
