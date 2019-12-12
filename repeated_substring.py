class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        number = len(s)
        i = 1
        isTrue = False
        while i <= (number/2):
            if number % i == 0:
                subString = s[:i]
                if (subString * (len(s) // i)) == s:
                    isTrue = True
                    break
            i = i + 1
        return isTrue
