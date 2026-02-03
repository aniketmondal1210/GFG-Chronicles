class Solution:
    def findKthMissing(self, arr1, arr2, k):
        # code here
        arr2_set = set(arr2)
        result = []
        for i in arr1:
            if i not in arr2_set:
                result.append(i)
            if len(result) == k:
                return result[-1]
        return -1
