class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a = list(map(str, A))
        a = int(''.join(a)) + K
        a = str(a)
        return [int(s) for s in a]
