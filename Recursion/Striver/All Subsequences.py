# Q) Print all the subsequences of given array.

new_seq = []
def subsequence(index,new_seq,arr):
    if index >= len(arr):
        print(new_seq)
        return
    #Take condition
    new_seq.append(arr[index])
    subsequence(index+1,new_seq,arr)
    new_seq.remove(arr[index])
    # Not take condition
    subsequence(index+1,new_seq,arr)

# # To Print the not-take sequences first
# def subsequence(index,new_seq,arr):
#     if index >= len(arr):
#         print(new_seq)
#         return
#     # Not take condition
#     subsequence(index + 1, new_seq, arr)
#     #Take condition
#     new_seq.append(arr[index])
#     subsequence(index+1,new_seq,arr)
#     new_seq.remove(arr[index])
#


ar1 = [3,1,2]
subsequence(0,new_seq,ar1)
