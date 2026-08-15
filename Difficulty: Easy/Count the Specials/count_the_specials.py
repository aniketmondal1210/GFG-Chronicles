import math
from collections import Counter
class Solution:
    def countSpecials(self, k, arr):
        # code here
        count = 0
        a = Counter(arr)
        b = set(arr)
        c = math.floor(len(arr)/k)
        for i in b:
            if a[i] == c:
                count += 1
        return count
