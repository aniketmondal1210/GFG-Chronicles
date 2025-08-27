from collections import Counter
class Solution:
    def checkDuplicates(self, arr):
        #code here
        a = Counter(arr)
        for key,value in a.items():
            if value > 1:
                return True
        return False
