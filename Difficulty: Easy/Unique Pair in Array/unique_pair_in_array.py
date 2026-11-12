from collections import Counter
class Solution:
    def findUniquePair(self, arr):
        """code here"""
        a = Counter(arr)
        unique_ele = [key for key, value in a.items() if value == 1]
        unique_ele.sort()
        return unique_ele
