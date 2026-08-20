from collections import Counter
class Solution:
    def canFormAnagram(self, a, b):
        """code here"""
        count_a = Counter(a)
        count_b = Counter(b)
        for key, value in count_a.items():
            if count_b[key] < value:
                return False
        return True
