class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reversed = x[::-1]
        if len(x) > 1:
            if reversed[0] == '-' or reversed[0] == '0':
                return False
            if x == reversed:
                return True
            else:
                return False
        else:
            return True
        
        