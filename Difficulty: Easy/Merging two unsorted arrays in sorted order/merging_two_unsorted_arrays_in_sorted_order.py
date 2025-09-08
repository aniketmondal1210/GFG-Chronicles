class Solution:
    def sortedMerge(self, arr1,arr2,res):
        # Your code goes here
        merged = arr1 + arr2
        merged.sort()
        res.clear()
        res.extend(merged)
