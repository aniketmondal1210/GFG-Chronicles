#User function Template for python3
from collections import Counter
class Solution:
    def findDuplicate(self, arr, k):
        # code here
        a = Counter(arr)
        num = float('inf')
        for key, value in a.items():
            if value == k:
                num = min(num, key)
        return num if num != float('inf') else -1
