#User function Template for python3
class Solution:
    def MaxNumber(self, arr):
        #code here.
        arr = [str(i) for i in arr]
        arr.sort(reverse=True)
        return ''.join(arr)
