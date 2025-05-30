from collections import Counter
class Solution:
    def findUnique(self, arr):
        # code here 
        a = Counter(arr)
        for key,value in a.items():
            if value < 2:
                return key
