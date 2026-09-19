from collections import Counter
class Solution:
    def findRepeating(self, arr):
        # code here 
        a = Counter(arr)
        for key, value in a.items():
            if value > 1:
                return [key, value]
        return [-1, -1]
