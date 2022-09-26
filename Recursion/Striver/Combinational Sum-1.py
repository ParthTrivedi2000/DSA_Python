# Q) https://leetcode.com/problems/combination-sum/

# def combinationsum(index,target,ds,array):
#     if index>=len(array):
#         if target ==

def comb(index, target, array, ds,ans):
    if index == len(array):
        if target==0:
            ans.append(ds[:])
        return

    # pick condition
    if array[index] <= target:
        ds.append(array[index])
        comb(index, target - array[index], array,ds,ans)
        ds.remove(ds[len(ds) - 1])
    # not pick condition
    comb(index + 1, target, array, ds,ans)

ar1 = [2,3,6,7]
# ar1 = [10,1,2,7,6,1,5]
l1 = []
target = 7
ans1 = []
x = comb(0,target,ar1,l1,ans1)
print(ans1)


# class Solution(object):
#
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         ds = []
#         answer = []
#
#         def comb(index, target, array, ds, ans):
#             if index >= len(array):
#                 if target == 0:
#                     # final_ans.extend(ds)
#
#                     # ans = ans+ds
#                     # ans.append(ds)
#                     # ans.append(ds)
#                     # print(ds)
#                     ans = ans + ans.extend(ds)
#                     # for numbers in ans:
#                     #     print(numbers)
#                     # return
#                 return
#
#             # pick condition
#             if array[index] <= target:
#                 ds.append(array[index])
#                 comb(index, target - array[index], array, ds, ans)
#                 ds.remove(ds[len(ds) - 1])
#             # not pick condition
#             comb(index + 1, target, array, ds, ans)
#
#         comb(0, target, candidates, ds, answer)
#         return answer
#
#         # return answer
#         # comb(0,target,candidates,ds,answer)
#         # return answer
#         # ans.append(x)
#         # return comb(0,target,candidates,[],ans)
#         # return

# in JAVA :-
#
#
# class Solution {
# public void combinationSum(int i, List < Integer > li, List < List < Integer >> ans, int target, int[] a, int n){
#
# if (i >= n){
# if (target == 0){
# ans.add(new ArrayList <> (li));
#
#
# return;
# }
# return;
# }
#
# for (int j=0; j < n; j++){
#     if (j > i & & a[j] == a[j + 1])continue;
#     if (a[i] > target) break;
#     li.add(a[i]);
#     combinationSum(i, li, ans, target - a[i], a, n);
#     li.remove(li.size() - 1);
# }
#
# combinationSum(i + 1, li, ans, target, a, n);
# }
# public
# List < List < Integer >> combinationSum2(int[]
# candidates, int
# target) {
#
# }
# }
