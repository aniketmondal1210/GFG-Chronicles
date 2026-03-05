from collections import Counter
class Solution:
    def countNonRepeated(self,arr):
        # code here
        a = Counter(arr)
        count = 0
        for key,value in a.items():
            if value == 1:
                count += 1
        return count
