def BinarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end-start)//2   # As if integer value stored in int mid vlaue is high enough to give error, hence we use this expression.
        # so simply just to avoid integer overflow problem, we have used this expression.
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1


arr1 = [2,3,4,5,9,14,16,18]
n = 14
x = BinarySearch(arr1,n)
print(x)