class Solution:
    def orderString(self, s):
    # code here
        s.sort()
        return [s[0], s[-1]]
