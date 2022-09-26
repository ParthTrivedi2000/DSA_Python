# Q) Print all the permutations of  given string.

# concept :- how this is different than previous or other subset problems?
# Actually if you have noticed, in previous questions we have fixed number of recrsion calls (2). But
# in this case (pls draw rec tree in ur notebook) we have variable recursion calls. we have to make those
# relationship with dependent variable to make recursion and then pass into the recursion as an arg.

def permutations(processed,unprocessed):
    if len(unprocessed)==0:
        print(processed)
        return

    char = unprocessed[0]

    # as jst explained abive hre we have variable rec call(variable rec call means suppose in first time u have
    # to call 2 times, then in next rec call it is not 2 times function call will be 3 or 5 times depending on the
    # expected output. so this is called varialbe rec cal). now whenver variable rec calls are there, then we have
    # to find dependent variable first and on basis of that we have to pass it into the next recursion call. for this
    # case as shown below we have recursion call dependent on the length of the processed variable (pls try to draw
    # on paper, u will came to know ki how recursion calls are changing or it is dependent on what or on which
    # available it is dependent). so then we will try to write the code bt considering this in mind and pass args also
    # in comply with that.

    for i in range(len(processed)+1):
        first_string = processed[:i]
        second_string = processed[i:]
        permutations(first_string+char+second_string,unprocessed[1:])

# permutations("","abcd")


# Q) Returning all the permutations.

def permutationsWithRet(processed,unprocessed):
    if len(unprocessed)==0:
        # print(processed)
        final_list = []
        final_list.append(processed[:])
        return final_list

    char = unprocessed[0]

    l1 = []

    for i in range(len(processed)+1):
        first_string = processed[:i]
        second_string = processed[i:]
        left = permutationsWithRet(first_string+char+second_string,unprocessed[1:])
        l1.extend(left)
    return l1



print(permutationsWithRet("","abc"))