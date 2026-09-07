from collections import Counter
class Solution:
    def halvesMatch(self, s):
        # code here
        mid = len(s) // 2
        if len(s) % 2 == 0:
            first_half = s[:mid]
            second_half = s[mid:]
        else:
            first_half = s[:mid]
            second_half = s[mid+1:]
        return Counter(first_half) == Counter(second_half)
