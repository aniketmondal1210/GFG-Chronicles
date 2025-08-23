class Solution:
    def commonSum(self,n1,n2,arr1,arr2):
        #code here
        a = set(arr1).intersection(set(arr2))
        return sum(list(a))%(10**9+7)
