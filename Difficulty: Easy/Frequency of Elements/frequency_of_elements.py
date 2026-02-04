from collections import Counter
class Solution:
    def countFreq(self, arr):
        #code here
        result = []
        a = Counter(arr)
        for key,value in a.items():
            result.append([key,value])
        return result
