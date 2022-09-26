# Q) Find the Floor number of given element from the array. Floor number means biggest number
# which is smaller or equal to the target element.

def Floor(arr,target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return arr[mid]
    return arr[end]


arr1 = [2,3,4,5,9,14,16,18]
n = 10
x = Floor(arr1,n)
print(x)
