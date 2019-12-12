def arraySum(numbers):
    sum = 0
    for s in numbers:
        sum += s
    return sum


def pivotIndex(nums):
    if len(nums) < 1:
        return -1
    leftSum = 0
    rightSum = arraySum(nums)
    i = 0
    # print(leftSum)
    # print(rightSum)
    while i < len(nums):
        # print(i)
        leftSum = arraySum(nums[:i])
        rightSum = rightSum - nums[i]
        if leftSum == rightSum:
            return i
        i = i + 1
    return - 1


def pivotIndexLeet(nums):
    S = sum(nums)
    leftSum = 0
    for i, x in enumerate(nums):
        if leftSum == (S - leftSum - x):
            print(leftSum)
            print(S - leftSum - x)
            return i
        # print("V : ", S - leftSum - x, " LEFT: ", leftSum)
        leftSum += x
    return -1


numbers = [1, 7, 3, 6, 5, 6]

print(pivotIndexLeet(numbers))
