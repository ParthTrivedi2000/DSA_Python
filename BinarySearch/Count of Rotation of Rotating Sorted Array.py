# def find(arr):
#     start = 0
#     end = len(arr) - 1
#     # x = 0
#     while(start<=end):
#         mid = start + (end-start)//2
#         nexta = (mid+1)%len(arr)
#         prev = (mid+len(arr)-1)%len(arr)
#         if arr[mid]<=arr[prev] and arr[mid]<=arr[nexta]:
#             return mid
#             # break
#         elif arr[mid]<=arr[end]:
#             end = mid-1
#         elif arr[start] <= arr[mid]:
#             start = mid + 1
#
#
#
#
# l1 = [11,14,15,18,2,5,6,8]
# l2 = [2,5,6,8,11,14,15,18]
# l3 = [11,14,2,5,6,8,9,10]
# num = 11
# print(find(l1))


def findPivotWithDuplicates(arr):
    start = 0
    end = len(arr) - 1
    while (start <= end):
        mid = start + (end - start) // 2
        # nexta = (mid + 1) % len(arr)
        # prev = (mid + len(arr) - 1) % len(arr)

    #     4 cases over here
        if mid<end and arr[mid] > arr[mid+1]:
            return mid
        if mid>start and arr[mid]<arr[mid - 1]:
            return mid-1

        # if elements at middle,start and end are equal, then jst skip the duplicates
        if (arr[mid] == arr[start] and arr[mid] == arr[end]):
            # skip the duplicates
            # but imp NOTE :- what if these elements at start and end are pivot?
            # check if start is pivot or not?
            if arr[start] > arr[start + 1]:
                return start
            start = start + 1

            # heck whether end is pivot
            if arr[end]<arr[end - 1]:
                return end - 1
            end = end-1

        # left side is sorted, so pivot should be in right
        elif arr[start]<arrr[mid] or arr[start]==ar[mid] and arr[mid] >arr[end]:
            start = mid+1
        else:
            end = mid - 1
    return -1

l1 = [2,2,2,9,2]
# num = 11
print(findPivotWithDuplicates(l1))