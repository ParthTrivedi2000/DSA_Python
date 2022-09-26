def BS(arr,target,start,end):
    while(start<=end):
        mid = start +(end-start)//2
        if target<arr[mid]:
            end = mid-1
        elif target>arr[mid]:
            start=mid+1
        else:
            return mid
    return -1


def find(arr,target):
    start = 0
    end = 1
    while(target>arr[end]):
        start = end
        end = end*2
    return BS(arr,target,start,end)


# Actual array is with infinite values it means [1,2,3,4,5,6,7,8,9,10,11,12.....]
l1 = [1,2,3,4,5,6,7,8,9,10,11]
num = 7
print(find(l1, num))
