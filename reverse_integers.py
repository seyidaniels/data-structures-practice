class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x == 0:
            return 0
        if x < 0:
            isNegative = True
            x = -(x)
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if rev >= (2 ** 31 - 1) / 10:
                return 0
            rev = rev * 10 + pop
        rev = -rev if isNegative else rev

        return rev


x = Solution()
print(x.reverse(123))
