from collections import Counter
class Solution:
    def find_unique(self, k, arr):
        #code here
        a = Counter(arr)
        for key,value in a.items():
            if value < 2:
                return key
