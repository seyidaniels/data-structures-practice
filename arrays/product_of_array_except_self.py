def productExceptSelf(self, nums: List[int]) -> List[int]:

    l, r, a = [0] * len(nums), [0] * len(nums), [0] * len(nums)

    length = len(nums)

    l[0] = 1
    for i in range(1, length):
        l[i] = nums[i-1] * l[i-1]

    r[length-1] = 1
    for i in reversed(range(length - 1)):
        r[i] = nums[i+1] * r[i+1]

    for i in range(length):
        a[i] = r[i] * l[i]

    return a
