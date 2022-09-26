def duplicate(nums):
    i = 0
    while (i < len(nums)):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            temp = nums[correct]
            nums[correct] = nums[i]
            nums[i] = temp
        else:
            i += 1
    lst = []
    for index in range(len(nums)):
        if nums[index] != index + 1:
            lst.append(nums[index])
    return lst

arr = [3,1,3,4,4,2]
x = duplicate(arr)
print(x)