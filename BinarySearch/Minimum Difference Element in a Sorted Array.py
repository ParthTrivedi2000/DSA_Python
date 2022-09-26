def binarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    while(start<=end):
        mid = start + (end-start)//2
        if target>arr[mid]:
            start = mid+1
        elif target<arr[mid]:
            end = mid-1
        else:
            return arr[mid]
    if abs(arr[start]-target) < abs(arr[end] - target):
        return arr[start]
    else:
        return arr[end]
l1 = [4,6,10]
num = 7
print(binarySearch(l1,num))