class Solution:
    def isPossible(self, arr):
        # code here 
        a = len(arr)
        return sum(arr) == a*(a+1)//2
