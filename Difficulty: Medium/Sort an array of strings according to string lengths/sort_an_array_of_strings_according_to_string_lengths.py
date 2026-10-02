class Solution:
    def sortByLength(self, arr):
       # code here
       arr.sort(key=lambda x: len(x))
       return arr
