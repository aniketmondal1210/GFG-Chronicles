class Solution:
    def getFirstSetBit(self,n):
        # code here
        a = bin(n)[2:][::-1]
        return a.index('1')+1
