#  Trapping Rain Water Problems has similarities with "Product of Array except SELF" problem


class Solution:
    def trap(self, height: List[int]) -> int:
        leftArray = (self.leftMaxArray(height))
        rightArray = (self.rightMaxArray(height))

        water = 0
        for i in range(len(height)):
            minWater = min(rightArray[i], leftArray[i])
            if minWater > height[i]:
                water += minWater - height[i]
        return water

    def rightMaxArray(self, array):
        result = [0] * len(array)
        rightMax = 0

        for i in reversed(range(len(array))):
            rightMax = max(array[i], rightMax)
            result[i] = rightMax
        return result

    def leftMaxArray(self, array):
        result = [0] * len(array)
        leftMax = 0

        for i in range(len(array)):
            leftMax = max(array[i], leftMax)
            result[i] = leftMax
        return result
