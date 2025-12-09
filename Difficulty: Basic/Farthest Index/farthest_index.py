#User function Template for python3
class Solution:
    def findIndex(self, arr, x):
        #code
        if x in arr:
            a = arr[::-1]
            return len(arr) - a.index(x)
        else:
            return -1
