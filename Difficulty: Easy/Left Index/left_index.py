#User function Template for python3
class Solution:
    def leftIndex (self, N, arr, X):
        # code here
        if X in arr:
            return arr.index(X)
        return -1
