def binarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    count = 0
    while(start<=end):
        mid = start+(end-start)//2
        if target>arr[mid]:
            start = mid+1
        elif target<arr[mid]:
            end = mid-1
        else:
            count = count+1
            if arr[mid]>arr[mid-1]:
                start = mid+1
            elif arr[mid]<arr[mid+1]:
                end = mid - 1
            # else:
            #     return count
    return count

l1 = [2,4,10,10,10,20,20]
num = 10
print(binarySearch(l1,num))

# Above method won't work. it is wrong

def BinarySearch(arr):
    start = 0
    end = len(arr)-1
