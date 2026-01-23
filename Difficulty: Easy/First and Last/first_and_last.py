#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        # Code here
        if x not in arr:
            return [-1]
        a = arr.index(x)
        b = len(arr) - 1 - arr[::-1].index(x)
        return [a,b]
