def missingAll(nums):
    i = 0
    while (i < len(nums)):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            temp = nums[i]
            nums[i] = nums[correct]
            nums[correct] = temp
        else:
            i += 1
    lst = []
    x = len(nums)
    for index in range(len(nums)):
        if (nums[index] != (index + 1)):
            lst.append(index + 1)
    return lst

arr = [4,3,2,7,8,2,3,1]
y = missingAll(arr)
print(y)