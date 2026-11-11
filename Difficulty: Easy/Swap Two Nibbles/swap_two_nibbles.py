class Solution:
    def swapNibbles (self, n):
        # code here 
        a = bin(n)[2:].zfill(8)
        b = a[:4]
        c = a[4:]
        d = c + b
        return int(d, 2) 
