def isPalindrone(string):
    return True if string == string[::-1] else False

# Strings of different Length can never be permutations of each other


def isPermutationOfOneAnother(string1, string2):
    if len(string1) != len(string2):
        return False
    if sorted(string1) != sorted(string2):
        return False
    return True

#  In more efficient cases, according to the solution


def permutation(string1, string2):
    map = {}

    for s in string1:
        map[s] = 1

    print(map)


p = permutation('dog', 'eod')

print(p)

# Edge Cases
# ------------
# Is it Case sensitive?
# Are there white spaces?
