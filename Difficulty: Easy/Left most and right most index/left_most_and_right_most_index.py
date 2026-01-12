#User function Template for python3
class Solution:
    def indexes(self, v, x):
        # Your code goes here
        if v.count(x) == 1:
            return v.index(x),v.index(x)
        elif v.count(x) == 0:
            return -1,-1
        else:
            a = v.index(x)
            b = len(v) - 1 - v[::-1].index(x)
            return a,b
