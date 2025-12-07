#User function Template for python3
class Solution:
    def medianOf2(self, a, b):
        #code here
        c = a + b
        c.sort()
        d = len(c) // 2
        if len(c) % 2 == 0:
            median = (c[d] + c[d-1]) / 2
        else:
            median = c[d]
        return median
