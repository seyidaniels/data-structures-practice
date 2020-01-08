class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums[:])
        left, right = 0, 0

        for i in range(len(sortedNums)):
            if sortedNums[i] != nums[i]:
                left = min(i, left)
                right = max(i, right)
        return right - left + 1 if right - left >= 0 else 0
