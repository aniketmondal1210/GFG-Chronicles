class Solution:    
    def modInverse(self,n,m):
        # code here
        for i in range(1,m):
            if (i*n) % m == 1:
                return i
        return -1
