class Solution:
    def remDuplicate(self, arr):
        # code here 
        a = list(set(arr))
        a.sort()
        return a
