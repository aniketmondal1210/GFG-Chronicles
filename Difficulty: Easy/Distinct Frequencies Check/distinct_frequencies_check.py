from collections import Counter
class Solution:
    def isFrequencyUnique(self, arr):
        # code here
        a = Counter(arr)
        result = []
        for key,value in a.items():
            result.append(value)
        return len(set(result)) == len(result)
