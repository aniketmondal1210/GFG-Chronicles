from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        #  code here
        a = Counter(arr)
        return [a[i] for i in range(1, len(arr) + 1)]
