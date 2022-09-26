# Note:- subsets are for arrays and subsequences are for strings.

# as we understood subset metjhod, simply jst take first element then make a call with take it and then another
# call to not take it. that's it. this is the subset method. we will follow for all the subsets and subsequences
# and permutation combination problems.

# Q) Print all the subsequences of the given string.

def subseq(processed,unprocessed):
    # what will be the base condition?
    # as we have understood subset method, from the method base condition should be when unprocessed (i.e. original
    # array or string which we have passed ) is empty then we should return our processed (array or string).
    if len(unprocessed)==0:
        print(processed)
        return
    # above we have written base condition.


    # So as per method we are taking first element
    ch = unprocessed[0]

    # call with taking it.
    subseq(processed+ch,unprocessed[1:])
    # call with not taking it
    subseq(processed,unprocessed[1:])

# subseq("","abc")


# Method - 2 :- above we are printing the list. in this method we are returning the list(or arry).
# concept used :- we will create one list object in the recursive function. as we know that list conains the value of
# particular that call only. as in each call new object is created so. so what we will do is we will not store
# anything while goint into the recursive call bt instead we will jst appending the answerswhile returning from
# the function.
def subseqWithrRet(processed,unprocessed):
    if len(unprocessed)==0:
        final_list = []
        final_list.append(processed)  # here exted won't work. it will consider processed as list and add all
        # the elements of it to the final_list(i.e. seperate elements 'a','b','c' everytime). bt actually processed
        # gives the string object (i.e. "abc" or "ab" or"ac" etc..) and that we don't want to store it by
        # seperating the elements. we want that whole element as it is. so append is used to add any element to
        # the list.
        return final_list

    ch = unprocessed[0]

    left = subseqWithrRet(processed+ch,unprocessed[1:])
    right = subseqWithrRet(processed,unprocessed[1:])

    left.extend(right)
    return left

print(subseqWithrRet("","abc"))