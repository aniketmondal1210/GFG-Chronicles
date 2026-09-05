class Solution:
    def alternateBits(self, n):
        # code here
        a = bin(n)[2:]
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                return False
        return True
