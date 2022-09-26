def find(arr,target,start,end):
    while(start<=end):
        mid = start + (end-start)//2
        if target<arr[mid]:
            end = mid-1
        elif target>arr[mid]:
            start = mid+1
        else:
            return mid
    return -1


def BS(arr,target):
    start = 0
    end = 1
    while(target!=arr[end]):
        start = end
        end = end*2
    return find(arr,target,start,end)

l1 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
num = 1
print(BS(l1,num))