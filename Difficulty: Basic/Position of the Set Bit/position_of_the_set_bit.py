class Solution:
    def findPosition(self, n):
        # code here 
        if n == 0:
            return -1
        a = bin(n)[2:]
        if a.count('1') != 1:
            return -1
        return len(a)
