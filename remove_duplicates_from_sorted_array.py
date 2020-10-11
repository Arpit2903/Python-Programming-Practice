def removeduplicates(nums):

    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.remove(nums[i])
        else:
            i = i + 1
    return len(nums)

print(removeduplicates([1,1,3,4,5]))