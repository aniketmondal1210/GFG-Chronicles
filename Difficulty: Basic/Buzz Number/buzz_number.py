class Solution:
    def isBuzz(self, n):
        #  code Here 
        if n % 10 == 7 or n % 7 == 0:
            return True
        return False
