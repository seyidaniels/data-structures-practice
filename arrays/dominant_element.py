class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        Max = max(nums)
        if (len(nums) > 1):
            sortednums = sorted(nums)
            sortednums.reverse()
            try:
                if ((Max / sortednums[1]) >= 2):
                    return nums.index(Max)
                return -1
            except:
                return nums.index(Max)
        return 0
