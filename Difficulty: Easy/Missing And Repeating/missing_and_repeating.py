from collections import Counter
class Solution:
    def findTwoElement(self, arr):
        # code here
        twice = 0
        missing = 0
        a = Counter(arr)
        for key,value in a.items():
            if value == 2:
                twice = key
        b = set(arr)
        for i in range(1,len(arr)+1):
            if i not in b:
                missing = i
                break
        return [twice,missing]
