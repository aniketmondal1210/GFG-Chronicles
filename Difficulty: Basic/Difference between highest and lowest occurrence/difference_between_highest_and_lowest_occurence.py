#User function Template for python3
from collections import Counter
class Solution:
    def findDiff(self, arr):
        # code here
        a = Counter(arr)
        b = max(a.values())
        c = min(a.values())
        return b - c
