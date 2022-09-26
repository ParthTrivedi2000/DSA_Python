# Q) Find the ceiling number of given element from the array. Ceiling number means smallest number
# which is greater or equal to the target element.

# Solution
# Logic:-
# 1) Step - 1 should be what is the target element?
# 2) next what all numbers are greater than the target
# 3) find the minimum of those greater elements. that's it.

# Approach :- see this is normal binary search problem only. in that also we r doing same thing. if u remember we
# are returning -1 if target element is not present right. so just think, here we need to return just greater element
# from the sorted array if target element is not present. That's it.

# Code:-
def Ceiling(arr,target):
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
    return arr[start]

# or

def Ceiling(arr,target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return arr[start]

# Understanding :-
# Why we had returned start index over here at last? or wht is the logic behind it?
# listen very carefully. See jb start < end hota he tb position of target element will be
# start --> ans --> end . but hme kya check krna he ki jb ye condition false hogi tb

# How I came to know ki yha pe muje return start kr dena ho to bhi ho jayega?
# see jese mene jo solution likha tha usme mid ko answer me store kr diya tha means ans = mid. then last me return it.
# aese bhi ho skta he. But yha pe dusre varible ka use ho rha he. usse accha ye upr jo solution likha he vo he
# jisme hm extra variable nhi use kr rhe he. To isme muje pta kese chla ki yha pe me aese return start kr du to chlega.
# See undersatnd very carefully. jb meri main condition yani start<=end vali koi bhi target ke liye
# true he it means tb sequence should be start ----> target -----> end. it means still I need to converge the solution
# towards the target element using BS. Suppose search space choti krte krte converge ho gya us time pe it might or might
# not happen ki start=target position(means mid)=end. Bt yha tk to thik he sbkuch, main sochne ki bat to abhi he.
# suppose koi iteration me abhi ye main condition false hui. It means end<start means sequence kya hua hoga ki
# end ----> start. tb ye start position he vo next vale ko indicate kr rhi hogi jo hme chahiye vo. isliye hmne
# start return krvaya.

arr1 = [2,3,4,5,9,14,16,18]
n = 10
x = Ceiling(arr1,n)
print(x)
