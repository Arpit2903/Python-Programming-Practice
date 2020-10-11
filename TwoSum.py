def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i,j]

    return None


print(twoSum([1,2,34,5], 7))