from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        # code here
        result = []
        a = Counter(arr)
        for key,value in a.items():
            if value > 1:
                result.append(key)
        return result
