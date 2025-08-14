class Solution:
    def kthElement(self, a, b, k):
        # code here
        c = a + b
        c.sort()
        return c[k-1]
