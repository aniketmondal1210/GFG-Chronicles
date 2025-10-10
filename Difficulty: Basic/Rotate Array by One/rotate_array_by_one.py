#User function Template for python3
class Solution:
    def rotate(self, arr):
        if len(arr) == 0:
            return
        
        arr[:] = arr[-1:] + arr[:-1]
