# Q) Search an element in a Rotated Binary Search Array

def search(arr,target,start,end):
    if start>end:
        return -1
    mid = start + (end-start)//2
    if arr[mid]== target:
        return mid

    if arr[start]<=arr[mid]:
        if target>=arr[start] and target<=arr[mid]:
            return search(arr,target,start,mid-1)
        else:
            return search(arr,target, mid+1, end)

    if target>=arr[mid] and target<=arr[end]:
        return search(arr,target,mid+1,end)
    return search(arr,target,start,mid-1)