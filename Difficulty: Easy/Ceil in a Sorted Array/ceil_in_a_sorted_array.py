#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        # code here
        for i in range(len(arr)):
            if arr[i] < x:
                continue
            return i
        return -1
