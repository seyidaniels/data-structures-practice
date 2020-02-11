class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convToInt(nums):
            tens = len(nums) - 1
            i = 0
            result = 0
            while i < len(nums):
                result += int(nums[i]) * 10 ** tens
                tens -= 1
                i += 1
            return result

        number1 = convToInt(num1)
        number2 = convToInt(num2)
        result = number1 * number2
        answer = ''
        if result == 0:
            return '0'
        while result != 0:
            d, m = divmod(result, 10)
            answer = str(m) + answer
            result = d
        return answer
