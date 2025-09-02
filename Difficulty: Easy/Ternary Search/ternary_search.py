class Solution:
    def findMinIndex(self, arr):
        # code here 
        min_ele = min(arr)
        return arr.index(min_ele)
