#User function Template for python3
from collections import Counter
class Solution:
    def findDuplicate(self, arr):
        #code here
        a = Counter(arr)
        for key, value in a.items():
            if value > 1:
                return key
