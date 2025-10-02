#User function Template for python3
class Solution:
    def multiply(self, arr):
        # Code here
        mid = len(arr)//2
        return sum(arr[:mid])*sum(arr[mid:])
