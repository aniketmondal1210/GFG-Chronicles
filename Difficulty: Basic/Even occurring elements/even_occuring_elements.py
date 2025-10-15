from collections import Counter

class Solution:
    def findEvenOccurrences(self, arr):
        # code here
        a = Counter(arr)
        result = []
        for key, value in a.items():
            if value % 2 == 0:
                result.append(key)
        if not result:
            return [-1]
        return result
