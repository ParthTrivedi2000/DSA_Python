def FirstAndLastPosition(arr,target):
    ans = [-1, -1]

    def search(nums, target, firstposition):
        start = 0
        end = len(nums) - 1
        ans = -1

        while (start <= end):
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if (firstposition):
                    end = mid - 1
                else:
                    start = mid + 1
        return ans

    ans[0] = search(arr, target, True)
    if ans[0] != -1:
        ans[1] = search(arr, target, False)
    return ans