#User function Template for python3
class Solution:
    def distinctCount(self, arr):
        # code here
        return len(set(x for x in arr if x > 0))
