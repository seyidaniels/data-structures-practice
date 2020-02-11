class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        result = [0] * len(A)
        i = len(A) - 1
        while i >= 0:
            if abs(A[left]) > A[right]:
                result[i] = A[left] * A[left]
                left += 1
            else:
                result[i] = A[right] * A[right]
                right -= 1
            i -= 1
        return result
