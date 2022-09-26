# Q - 1) Print all those subsequences from given array which has sum equal to K.
# Solution:-


# array,s and n are given in the question which are passing in the recursive function
def subsequence(index,new_seq,sm,array,s):
    if index>=len(array):
        if sm==s:
            print(new_seq)
        return
    #Take condtion
    new_seq.append(array[index])
    sm = sm + array[index]
    subsequence(index+1,new_seq,sm,array,s)
    new_seq.remove(array[index])
    sm = sm - array[index]
    # Not take condition
    subsequence(index+1,new_seq,sm,array,s)

new_seq = []
ar1 = [1,2,1]
sum_given = 2
subsequence(0,new_seq,0,ar1,sum_given)

# Q - 2) Now suppose in question given that, out of so many sequences you have to print any one subsequence only.
# solution:-

# def subsequence(index,new_seq,sm,array,sum_given):
#     if index >= len(ar1):
#         if sm == sum_given:
#             print(new_seq)
#             return True
#         return False
#     new_seq.append(array[index])
#     sm = sm + array[index]
#     if subsequence(index+1,new_seq,sm,array,sum_given) == True:
#         return True
#     new_seq.remove(array[index])
#     sm = sm - array[index]
#     if subsequence(index+1,new_seq,sm,array,sum_given) == True:
#         return True
#
# new_seq = []
# ar1 = [1,2,1]
# sum_given = 2
# subsequence(0,new_seq,0,ar1,sum_given)