class Solution:
    def transitionPoint(self, arr): 
        # Code here
        if all(x == 0 for x in arr):
            return -1
        elif all(x == 1 for x in arr):
            return 0
        else:
            return arr.index(1)
