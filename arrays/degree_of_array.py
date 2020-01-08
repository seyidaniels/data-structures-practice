class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        numsFreq = {}
        seenIndexes = {}

        minLength = 0

        for i in range(len(nums)):
            if nums[i] not in seenIndexes:
                seenIndexes[nums[i]] = i
            if nums[i] not in numsFreq:
                numsFreq[nums[i]] = 1
            else:
                numsFreq[nums[i]] += 1

            if numsFreq[nums[i]] > degree:
                degree = numsFreq[nums[i]]
                minLength = i - seenIndexes[nums[i]] + 1
            elif numsFreq[nums[i]] == degree:
                minLength = min(minLength, i - seenIndexes[nums[i]] + 1)
            i += 1

        return minLength
