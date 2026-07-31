class Solution:
    def leftElement(self,arr):
        # code here
        arr.sort()
        n = len(arr)
        return arr[(n-1)//2]
