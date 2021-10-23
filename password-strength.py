'''
In order to ensure account security, the developers at Amazon have come up with a new algorithm to determine the strength of a password. 
According to this algorithm, the strength of a password consisting of lowercase English letters only, is calculated as the sum of the number of distinct characters present in all possible substrings of that password. 
Given a string password, find the strength of that password. 
Note: A substring is a contiguous sequence of characters within a string, taken in the same order. 
Example password ="good" 
The possible substrings with distinct character count are: 
substring Count of Distinct Substring coon amino Characters Characters good good good good good good good good good good 
2 
2 
2 
3 
Here, red-colored characters denote the substring to be considered. 
Thus, password strength = 1 + 1 + 1 + 1 +2.1 + 2 + 2 + 2 + 3 = 16. 



good

g => 1

go => 2

goo => 2

good => 3

o => 1

oo => 1

ood =>2

o => 1

od => 2

d => 1


16


good
'''


def password_strength(password):
    last = {chr(97 + i): -1 for i in range(26)}
    ret = 0
    for i, ch in enumerate(password):
        left = i - last[ch]
        right = len(password) - i
        ret += left * right
        last[ch] = i

    return ret


result = password_strength('good')

print(result)
