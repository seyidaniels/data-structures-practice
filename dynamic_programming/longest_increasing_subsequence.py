class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        LIS = [1] * len(nums)

        i = 1

        while i < len(nums):
            j = 0
            while j < i:
                if nums[j] < nums[i] and LIS[j] + 1 > LIS[i]:
                    LIS[i] = LIS[j] + 1
                j += 1
            i += 1
        print(LIS)
        return max(LIS)
