class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        if len(A) >= 3:
            N = len(A)
            i = 0

            while i+1 < N and A[i] < A[i+1]:
                i += 1

            if i == 0 or i == N-1:
                return False

            while i+1 < N and A[i] > A[i+1]:
                i += 1

            return True if i == N-1 else False
