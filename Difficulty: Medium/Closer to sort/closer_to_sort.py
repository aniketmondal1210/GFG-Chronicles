class Solution:
    def closer(self, arr, x):
        # code here
        if x in arr:
            return arr.index(x)
        return -1
