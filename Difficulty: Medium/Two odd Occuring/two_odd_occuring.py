from collections import Counter
class Solution:
    def twoOddNum(self, arr):
        #code here 
        a = Counter(arr)
        result = []
        for key, value in a.items():
            if value % 2 != 0:
                result.append(key)
        return sorted(result,reverse=True)
