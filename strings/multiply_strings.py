class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        maxLength = len(num1) if len(num1) >= len(num2) else len(num2)

        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1

        if maxLength == len(num1):
            num2 = num2.zfill(maxLength)
        else:
            num1 = num1.zfill(maxLength)

        i = len(num2) - 1

        superSum = []

        while i >= 0:
            n1 = int(num2[i])
            j = len(num1) - 1
            carry = 0
            result = []
            while j >= 0:

                n2 = int(num1[j])

                singleM = n1 * n2 + carry

                if singleM >= 10:
                    singleM = str(singleM)
                    carry = int(singleM[0])
                    singleM = singleM[1]

                else:
                    carry = 0

                result.insert(0, str(singleM))

                j -= 1
            # if carry == 1:
            #     result.insert(0, str(1))
            superSum.append(''.join(result))
            i -= 1

        i = 1

        print(superSum)

        finalSum = superSum[0]

        while i < len(superSum):
            zeroFill = '0'
            zeroFill = zeroFill.zfill(i)
            finalSum = self.addStrings(finalSum, superSum[i] + zeroFill)
            i += 1

        return finalSum.lstrip('0')

    def addStrings(self, num1: str, num2: str) -> str:
        maxLength = len(num1) if len(num1) >= len(num2) else len(num2)

        if maxLength == len(num1):
            num2 = num2.zfill(maxLength)
        else:
            num1 = num1.zfill(maxLength)

        maxLength -= 1

        result = []
        carry = 0

        while maxLength >= 0:
            n1 = int(num1[maxLength])
            n2 = int(num2[maxLength])
            singleAdd = n1 + n2 + carry
            if singleAdd >= 10:
                singleAdd = singleAdd - 10
                carry = 1
            else:
                carry = 0
            result.insert(0, str(singleAdd))

            maxLength -= 1

        if carry == 1:
            result.insert(0, str(1))

        return (''.join(result))
