# Q) Search an element from an array through Linear Search using recursion.(note here array may or may not be sorted).

# (by me)
def find(arr,target,index):
    if index==len(arr):
        return False
    elif arr[index] == target:
        return index
    else:
        return find(arr,target,index+1)

arr1 = [3,5,81,23,41]
print(find(arr1,82,0))

# By KK
def find(arr,target,index):
    if index==len(arr):
        return -1
    return arr[index]==target or find(arr,target,index+1)

p = [3,5,81,23,41]
print(find(p,82,0))

# or if u want to return index then
def findIndex(arr,target,index):
    if index==len(arr):
        return -1
    if arr[index]==target:
        return index
    else:
        return findIndex(arr,target,index+1)

x = [3,5,81,23,41]
print(find(x,82,0))

# Searching from last
def findIndexLast(arr,target,index):
    if index== -1:
        return -1
    if arr[index]==target:
        return index
    else:
        return findIndexLast(arr,target,index-1)

arr2 = [3,5,81,23,41]
print(find(arr2,82,0))

# To abhi ye above vale codes duplicte element ke liye sirf ek hi position denge 1st vali. agr dono chahiye to?
# see below code.

l1 = []
def findAllIndex(arr,target,index):
    if index==len(arr):
        return
    if arr[index]==target:
        l1.append(index)
    findAllIndex(arr,target,index+1)

a = [3,5,81,81,23,41]
findAllIndex(a,81,0)
print(l1)

# Now in above case hmne list bahar declare kiya he.then ander use kiya he. Bt now suppose wht if I don't want to use
# externally created list or array.

# Concept :- this is the concept which covers returning list or array in recursion problems
# Q) So now the question is we need to return list or array means my function's return type should be list or array.
# it's not like I will create outside list and then functoin returning nothing and outside I will print that list. No.

# Solution:- So there are 2 approaches to achieve above task.
# 1) to pass that list as a parameter to the function.
# 2) create one function inside the main recusrion function and don't change parameters of the recursive function.

# Concept:-So the difference between those 2 methods is, while passing as a parameter, then it will also passed to next
# all future recursive call. While the variables created inside a function is available and valid for that function and
# function call only.

def findAlIndex(arr,target,index,l1):
    if index==len(arr):
        return l1
    if arr[index]==target:
        l1.append(index)
    findAlIndex(arr,target,index+1,l1)

a = [3,5,81,81,23,41]
findAlIndex(a,81,0,[])
print(l1)

# Now V V V IMP concept:-Return list without passing the arguments.:-
# So Goal is:- return the list. Bt don't take list in the argument.

def findAlIndex2(arr,target,index):
    l1 = []
    if index==len(arr):
        return l1
    # this will contain answer for that function call only.
    if arr[index]==target:
        l1.append(index)
    answerFromBelowCalls = findAlIndex2(arr,target,index+1)
    l1.extend(answerFromBelowCalls)
    return l1

a = [3,5,81,81,23,41]
# findAlIndex2(a,81,0)
print(findAlIndex2(a,81,0))
# wht we have done here is in each call one new object is created. to vo hr bar empty hi bnega. to abhi hmne kya
# kiya ke niche jate time(i.e. next calls) means recursion me jate time answer store na krke return hote time
# answer store kiya he kyuki yha pe ye case he ki answer vo particulr function call ke ander hi he dusre call
# me nya empty object create ho rha he. To particular function return hote time ek object me answer
# return kraya and vo object ko next return call me bhej diya.

# Generally this above approach is not used as it is not optimised as in each call new object is created. Bt still
# in many problems this approach will be there. so covered here.
