def missing(arr):
    i = 0
    while(i<len(arr)):
        correct = arr[i]
        if arr[i] == len(arr):
            i+=1
        elif arr[i] != arr[correct]:
            temp = arr[i]
            arr[i] = arr[correct]
            arr[correct] = temp
        else:
            i+=1
    x = len(arr)
        # return len(arr)
    for i in range(len(arr)):
        if i != arr[i]:
            return i
    for j in arr:
        if x!=j:
            return x
        # return x
    # return len(arr) if len(arr) not in arr

# a1 = [1,2,3,5]
# x = missing(a1)
# print(x)


# code

def swap(arr,start,end):
    temp = arr[start]
    arr[start]=arr[end]
    arr[end] = temp

def missingNumber(arr):
    i = 0
    while(i<len(arr)):
        correct_index = arr[i]
        # below we have added element<len(arr) bec agr last element hoga to uski index to available hogi hi nhi
        # or error index out of bound aa jayega so yha pe logic lgaya he ki jb bhi last index ka element ho to
        # usko ignor kreke i ko move forward kra dena he.
        if arr[i]<len(arr) and arr[i]!= arr[correct_index]:
            swap(arr,i,correct_index)
        else:
            i+=1

    # Search first missing element from array
    for index in range(len(arr)):
        # index = i
        if arr[index] != index:
            return index
    #  case-2 :- if missing element is last element it means from [0,1,2,3] given out of 0 to 4 integers, then wht ...
    #  so we have included below check.
    return len(arr)

a1 = [0,1,2,3,4]
x = missingNumber(a1)
print(x)