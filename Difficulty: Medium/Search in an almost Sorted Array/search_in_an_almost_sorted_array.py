#User function Template for python3
class Solution:
    def findTarget(self, arr, target):
        # code here
        if target in arr:
            return arr.index(target)
        return -1
