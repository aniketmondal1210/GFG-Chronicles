from collections import Counter
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        a = Counter(arr)
        for key,value in a.items():
            if value % 2 != 0:
                return key
