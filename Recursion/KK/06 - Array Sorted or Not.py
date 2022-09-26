# Q) Check whether given array is sorted or not?

# (by me)
def sorti(arr,start):
    if start==len(arr)-1:
        return True
    elif arr[start]<=arr[start+1]:
        return sorti(arr,start+1)
    else:
        return False

# x = [2,5,6,8,11,116,14,15,18]
x = [1,2,4,3]
print(sorti(x,0))

# Method - 2) by KK

def sort(arr,index):
    if index==len(arr)-1:
        return True
    return arr[index]<arr[index+1] and sort(arr,index+1)

x = [1,2,4,3]
print(sort(x,0))

# Please here note one thing ki arr object he usme means originl array jo pas kiya he usme koi change nhi ho rha he
# Task jo perform kiya he vo dusri argument se ho gya he. inshort original object me change nhi ho rha he.
# So here in every function call, arr is the reference which jst point out the same array which resides in the memory.
# So if I modify arr in any one recursion call, it will be modified for all other calls and at last in answer time
# pe bhi it will be seen as modified arr. so ye dikkat bad me aa skti he isliye ye thoda concept btaya he to dekh ke
# recursion me args pas krna and dekh ke recursion ke ander ka code likhna.