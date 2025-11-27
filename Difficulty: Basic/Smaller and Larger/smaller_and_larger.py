#User function Template for python3
class Solution:
    def getMoreAndLess(self, arr, target):
        less_equal = 0
        greater_equal = 0
    
        for x in arr:
            if x <= target:
                less_equal += 1
            if x >= target:
                greater_equal += 1
    
        return [less_equal, greater_equal]
