class Solution:
    def reverseBits(self,n):
        #code here
        a = bin(n)[2:]
        b = a[::-1]
        return int(b,2)
