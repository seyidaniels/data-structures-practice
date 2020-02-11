def threeSum(nums):
    nums.sort()
    answers = []
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            anchor = -nums[i]
            low = i+1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == anchor:
                    answers.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    high -= 1
                    low += 1
                elif nums[low] + nums[high] > anchor:
                    high -= 1
                elif nums[low] + nums[high] < anchor:
                    low += 1

    return answers


print(threeSum([0, 0, 0]))+
