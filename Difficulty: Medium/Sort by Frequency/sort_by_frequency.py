from collections import Counter
class Solution:
    def frequencySort(self, s):
        # code here
        a = Counter(s)
        sorted_s = sorted(s,key = lambda x: (a[x],x))
        return "".join(sorted_s)
