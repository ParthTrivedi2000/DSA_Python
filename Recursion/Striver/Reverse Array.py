# method - 1 :- using 2-pointers

def swap(start,end,arr):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp


def reverse_array(start,end,arr):
    if start>=end:
        return
    swap(start,end,arr)
    reverse_array(start+1,end-1,arr)


# but now suppose in question given is like only use 1 - pointer to reverse the array then we can do it by using below mthd.

# method - 2:- using 1-pointer

def rev_array(i,arr,n):
    if i>=n//2:
        return
    swap(i, n - i - 1, arr)
    rev_array(i+1,arr,n)
arr1 = [13,45,34,23,6]
n = len(arr1)
# x = reverse_array(0,len(arr1)-1,arr1)
y = rev_array(0,arr1,n)
print(arr1)