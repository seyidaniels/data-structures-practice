class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) > 0:
            maxCurrent = nums[0]
            maxGlobal = nums[0]

            for i in range(1, len(nums)):
                maxCurrent = max(nums[i]+maxCurrent, nums[i])

                if maxCurrent > maxGlobal:
                    maxGlobal = maxCurrent
            return maxGlobal
        return 0
        