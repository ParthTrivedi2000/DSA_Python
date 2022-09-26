# Q) Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

def smallest(letters,target):
    start = 0
    end = len(letters) - 1

    # if target>letters[len(letters)-1]:
    #     return -1
    while (start <= end):
        mid = start + (end - start) // 2
        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % len(letters)]

l1 = ['c','f','j']
char = 'a'
print(smallest(l1,char))