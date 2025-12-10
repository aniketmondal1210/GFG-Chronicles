#User function Template for python3
class Solution:
    def intersection(self,a, b):
        a = list(set(a).intersection(set(b)))
        a.sort()
        return a
