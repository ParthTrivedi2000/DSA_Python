# note :-
# 1] whenever in question if you find word like 'given in range of 1 to N' then you have to apply cyclic sort
# method. i short question will be whaterever bt if u find any range is given then u have to apply this algo.
# 2] if in question time complexity was given as O(n) then also u should understand that in this qustion I have to
# apply cyclic sort method.
# 3] formula :- index = value - 1 (bt this is for range 1 to N)
# 4] if range is given 0 to N then u should make formula as per given range.
# 5] and one last thing is this method or algorithm is applicable to "any given continous range". bt remember as per
# the range u have to modify or change the formula.for example:- range is given 11 to N then formula should be
# index = value - 11

def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    return arr


def cyclic(arr):
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i]    # we find the correct index for the value. (or as discussed above we are applying that
        # formula of relation between index and value. here it is considered that range is given from 0 to N
        # hence relation or formula between index and value is index = value only.
        if (arr[i] != arr[correctIndex]):
            swap(arr, i, correctIndex)
        else:
            i += 1
    return arr


a1 = [3,0,2,1]
x = cyclic(a1)
print(x)