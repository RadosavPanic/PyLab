# Codebook for encoding/decoding letters
"""
Dictionary holds random pairs of letters, where each letter
in the alphabet needs to contain own pair that is random chosen.
Duplicates are not allowed for pairs.
"""

import random

letters = list(map(chr, range(97, 123)))  # lowercase ASCII letters
codebook = []
chosen = set()

for letter in letters:
    temp = list(set(letters).difference(chosen).difference(set(letter)))
    if len(temp):
        value = random.choice(temp)
    else:
        break
    chosen.update(set(value))
    codebook.append((letter, value))
    """
    1st difference: subtracts elements in chosen set, which keeps track of letters used in letters set
    2nd difference: subtracts current letter from result obtained in previous step with chosen set
    Purpose: removing current letter from consideration of pairing with itself in the codebook
    """

codebook = dict(codebook)

# decodebook = inverted codebook (key->value, value->key)
decodebook = {}

for key, value in codebook.items():
    decodebook[value] = key

# Encoding phase with codebook
message = input("Insert message: ")
encoded_message = []

for letter in message:
    try:
        encoded_message.append(codebook[letter])
    except KeyError:
        encoded_message.append(letter)

printable_encoded_message = "".join(encoded_message)
print(f"Encoded message: {printable_encoded_message}")


# Decoding phase

decoded_message = []

for letter in printable_encoded_message:
    try:
        decoded_message.append(decodebook[letter])
    except KeyError:
        decoded_message.append(letter)

printable_decoded_message = "".join(decoded_message)
print(f"Decoded message: {printable_decoded_message}")
