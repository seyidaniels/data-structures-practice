
# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each
# letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front
# of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
#
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
#

# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

def caesar_cipher(s, k):
    UPPER = 65
    LOWER = 97
    result = []
    for character in s:
        if character.isalpha():
            start = UPPER if character.isupper() else LOWER
            newCharacterAscii = start + ((26 + abs(start - (ord(character) + k))) % 26)
            result.append(chr(newCharacterAscii))
            continue
        result.append(character)
    return ''.join(result)

