from collections import Counter
class Solution:
    def countFreq(self, arr):
        # Code here
        a = Counter(arr)
        result = []
        summ = 0
        for key in sorted(a):
            summ += a[key]
            result.append(summ)
        return result
