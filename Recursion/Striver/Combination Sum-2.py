# def comb(index, target, array, ds, ans):
#     if index == len(array):
#         if target==0:
#             ans.append(tuple(ds[:]))
#             # list(ans)
#         return
#
#     # pick condition
#     if array[index] <= target:
#         ds.append(array[index])
#         comb(index+1, target - array[index], array,ds,ans)
#         ds.remove(ds[len(ds) - 1])
#     # not pick condition
#     comb(index + 1, target, array, ds,ans)
#
# ar1 = [10,1,2,7,6,1,5]
# ar1.sort()
# l1 = []
# target = 8
# ans1 = []
# x = comb(0,target,ar1,l1,ans1)
# # list(ans1)
# # print(tuple(ans1))
# # print(set(tuple(ans1)))
# y = []
# list(set(ans1))
# for i in list(set(ans1)):
#     y.append(list(i))
# print(y)


## 2nd method (main method):-

def combi(index,target,array,ds,ans):
    if target==0:
        # ds.append(array[index])
        ans.append(ds[:])
        # print(ds)
        return
    for i in range(index,len(array)):
        if array[i]>target:
            break
        if i>index and array[i]==array[i-1]:
            continue
        ds.append(array[i])
        combi(i+1,target-array[i],array,ds,ans)
        ds.remove(array[i])

ar1 = [10,1,2,7,6,1,5]
# ar1 = [1,1,1,2,2]
ar1.sort()
l1 = []
target = 8
ans1 = []
x = combi(0,target,ar1,l1,ans1)
print(ans1)