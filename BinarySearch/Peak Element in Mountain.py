# def peak(arr):
#     start = 0
#     end = len(arr) - 1
#     while(start < end):
#         mid = start + (end - start)//2
#
#         if arr[mid]<arr[mid+1]:
#             start = mid + 1
#         elif arr[mid]>arr[mid+1]:
#             end = mid
#     return end
#
# ar1 =  [1,5,7,10,13,11,8]
# x = peak(ar1)
# print(x)

# Method - 2) Aditya Verma :-
def peak(arr):
    start = 0
    end = len(arr) - 1
    while(start<=end):
        mid = start + (end-start)//2
        if arr[mid]>arr[0] or arr[mid]<arr[len(arr) - 1]:
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return arr[mid]
            elif arr[mid]<arr[mid+1]:
                start = mid+1
            elif arr[mid]<arr[mid-1]:
                end = mid - 1
        elif arr[mid] == arr[0]:
            if arr[mid]<arr[mid-1]:
                return arr[mid-1]
            else:
                return arr[mid]
        elif arr[mid] == arr[len(arr) - 1]:
            if arr[mid]<arr[mid-1]:
                return arr[mid-1]
            else:
                arr[mid]

l1 = [1,5,10,12,8,7]
print(peak(l1))