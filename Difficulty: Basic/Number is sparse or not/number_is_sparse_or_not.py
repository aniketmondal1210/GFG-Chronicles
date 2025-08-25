class Solution:
    def isSparse(self,n):
        # code here 
        a = bin(n)[2:]
        if '11' in a:
            return False
        return True
