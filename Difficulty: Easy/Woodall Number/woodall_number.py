class Solution:
    def isWoodall(self, n):
        # code here
        k = 1
        while True:
            woodall = k*(2**k) - 1
            if woodall == n:
                return True
            if woodall > n:
                return False
            k += 1
