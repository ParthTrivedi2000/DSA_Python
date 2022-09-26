# Q) Print all the subsets of an array.
# SOlution :- same s we have done for strings.
def subset(processed,unprocessed):
    if len(unprocessed)==0:
        print(processed)
        return

    element = unprocessed[0]
    processed.append(element)
    subset(processed,unprocessed[1:])
    processed.remove(element)
    subset(processed,unprocessed[1:])

# l1 = []
# subset([],[1,2,3])


# Q) return the subsequences of an array instead of print.

def subsetWithRet(processed, unprocessed):
    if len(unprocessed) == 0:
        # print(processed)
        final_list = []
        final_list.append(processed[:])
        return final_list

    element = unprocessed[0]

    processed.append(element)
    left = subsetWithRet(processed, unprocessed[1:])
    processed.remove(element)
    right = subsetWithRet(processed, unprocessed[1:])

    left.extend(right)
    for i in range(0,len(left)-1):
        if left[i] == left[i+1]:
            left.remove(left[i+1])
    return left


print(subsetWithRet([], [1, 2, 2]))
