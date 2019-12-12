def twoSum(nums, target):
    answer = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums and (nums.index(diff) - i) != i:
            answer.append(i)
            answer.append(nums.index(diff))
            return answer

    #     if diff in nums[i+1:]:


print(twoSum([3, 9, 2], 5))
