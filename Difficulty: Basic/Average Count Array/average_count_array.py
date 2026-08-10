import math
from collections import Counter
class Solution:
    def countArray(self, arr, x):
        # code here
        a = Counter(arr)
        result = []
        for i in range(len(arr)):
            b = math.floor(arr[i]+x)//2
            result.append(a[b])
        return result
