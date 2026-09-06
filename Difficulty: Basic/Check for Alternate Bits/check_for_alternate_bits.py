class Solution:
    def alternateBits(self, n):
        # code here
        if n == 0:
            return 0
        x = n ^ (n >> 1)
        return (x & (x+1)) == 0
