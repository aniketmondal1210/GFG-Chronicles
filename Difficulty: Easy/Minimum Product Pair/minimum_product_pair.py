class Solution:
    def printMinimumProduct(self, arr):
        # code here
        arr.sort()
        return arr[0]*arr[1]
