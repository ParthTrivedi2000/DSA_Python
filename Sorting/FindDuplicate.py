def duplicate(nums):
    i = 0
    while (i < len(nums)):
        if nums[i] != i + 1:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                temp = nums[correct]
                nums[correct] = nums[i]
                nums[i] = temp
            else:
                return nums[i]
        else:
            i+=1


arr = [3,1,3,4,2]
x = duplicate(arr)
print(x)