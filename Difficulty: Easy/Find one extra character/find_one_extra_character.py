from collections import Counter
class Solution: 
    def extraChar(self,s1, s2):
        # code here
        a = Counter(s1)
        b = Counter(s2)
        for i in b:
            if b[i] != a[i]:
                return i
        return ''
