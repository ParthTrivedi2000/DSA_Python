def mismatch(nums):
    i = 0
    lst = []
    while (i < len(nums)):
        # if nums[i] != i+1:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            temp = nums[correct]
            nums[correct] = nums[i]
            nums[i] = temp
        # else:
        #     lst.append(nums[i])
        else:
            i += 1

    for index in range(len(nums)):
        if nums[index] != index + 1:
            lst.append(nums[index])
            lst.append(index + 1)
    return lst

arr = [1,2,2,4]
x = mismatch(arr)
print(x)