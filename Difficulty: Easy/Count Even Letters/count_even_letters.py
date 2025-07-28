from collections import Counter
class Solution:
    def count(self, s):
        # code here
        a = Counter(s)
        count = 0
        for key,value in a.items():
            if value % 2 == 0:
                count += 1
        return count
