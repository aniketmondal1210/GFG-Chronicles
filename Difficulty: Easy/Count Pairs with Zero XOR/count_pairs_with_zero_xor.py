from collections import Counter
class Solution:
    def countPairs(self, arr):
        # code here
        a = Counter(arr)
        count = 0
        for key, value in a.items():
            if value >= 2:
                count += value*(value-1)//2
        return count
