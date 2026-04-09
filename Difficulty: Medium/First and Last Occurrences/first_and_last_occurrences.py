class Solution:
    def find(self, arr, x):
        # code here
        if x not in arr:
            return [-1,-1]
        a = arr.index(x)
        b = len(arr) - arr[::-1].index(x) - 1
        return [a,b]
