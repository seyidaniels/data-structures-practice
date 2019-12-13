class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = max(len(a), len(b))
        carry = 0
        finalSum = []
        while len(a) < i:
            a = "0" + a
        while len(b) < i:
            b = "0" + b
        i = i - 1
        while i >= 0:
            val1 = int(a[i])
            val2 = int(b[i])
            carry, singleSum = divmod((val1+val2+carry), 2)
            finalSum.insert(0, str(singleSum))
            i -= 1
        if carry != 0:
            finalSum.insert(0, str(carry))
        final = ''
        return final.join(finalSum)
