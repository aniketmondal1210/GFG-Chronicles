class Solution:
    def thirdLargest(self,arr):
        # code here
        arr.sort()
        return arr[-3]
