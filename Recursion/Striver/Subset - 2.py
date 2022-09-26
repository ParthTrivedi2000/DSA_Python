def Subset(index,array,ds,ans):
    # print(ds)
    ans.append(ds[:])
    # if index==len(array):
    #     # ds.append()
    #     print(ds)
    #     return
    for i in range(index,len(array)):
        if i!=index and array[i]==array[i-1]:
            continue
        # if index in ds:
        #     continue
        ds.append(array[i])
        Subset(i+1,array,ds,ans)
        ds.remove(ds[len(ds)-1])
        # Subset(i+1,array,ds,ans)

# ar1 = [1,2,2]
ar1 = [4,4,4,1,4]
l1 = []
ans1 = []
x = Subset(0,ar1,l1,ans1)
print(ans1)

# Input
# [4,4,4,1,4]
# Output
# [[],[4],[4,4],[4,4,4],[4,4,4,1],[4,4,4,1,4],[4,1,4,4],[1,4,1],[1,4,1,4],[1,1,4],[1,1],[1,1,4],[1,4],[1],[1,4],[4]]
# Expected
# [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]