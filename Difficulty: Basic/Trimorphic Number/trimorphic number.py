class Solution:
    def isTrimorphic(self, n):
        # code here
        s = str(n)
        return str(n**3)[-len(s):] == s
