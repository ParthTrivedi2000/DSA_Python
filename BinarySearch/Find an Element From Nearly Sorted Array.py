# def BS(arr, target, start, end):
#     while (start <= end):
#         mid = start + (end - start) // 2
#         if target < arr[mid]:
#             end = mid - 1
#         elif target > arr[mid]:
#             start = mid + 1
#         else:
#             return mid
#     return -1
#
#
# def find(arr, num):
#     start = 0
#     end = len(arr) - 1
#     x = 0
#     while (start <= end):
#         mid = start + (end - start) // 2
#         nexta = (mid + len(arr) + 1) % len(arr)
#         prev = (mid + len(arr) - 1) % len(arr)
#         if arr[mid] < arr[prev] and arr[mid] < arr[nexta]:
#             x = mid
#             break
#         elif arr[mid] <= arr[end]:
#             start = mid + 1
#         elif arr[start] <= arr[mid]:
#             end = mid - 1
#     a = BS(arr, num, 0, x - 1)
#     b = BS(arr, num, x, len(arr) - 1)
#     if a == -1 and b == -1:
#         return -1
#     elif b == -1:
#         return a
#     else:
#         return b

    # return -1

# l1 = [11, 14, 15, 18, 2, 5, 6, 8]
# l2 = [5, 10, 30, 20, 40]
# num = 50
# print(find(l2, num))


# Method - 2)
def binarySearch(arr,target):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = start + (end-start)//2
        nexta = (mid+1)%len(arr)
        prev = (mid+len(arr)-1)%len(arr)
        if target==arr[mid]:
            return mid
        elif prev<=start and target==arr[prev]:
            return prev
        elif (nexta)>=start and target==arr[nexta]:
            return nexta
        elif target<arr[mid]:
            end = mid-2
        elif target>arr[mid]:
            start = mid+2
    return -1

l2 = [5, 10, 30, 20, 40]
num = 5
print(binarySearch(l2, num))