from collections import Counter

class Solution:
    def canFormPalindrome(self, s):
        # code here
        a = Counter(s)
        odd_count = sum(1 for value in a.values() if value % 2 != 0)
        return odd_count <= 1
