from collections import Counter
class Solution:
    def equalPairs(self, s):
        # code here
        return sum(i * i for i in Counter(s).values())
