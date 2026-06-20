class Solution:
    def getLastDigit(self, a, b):
        # code here
        base = int(a)
        exponent = int(b)
        return pow(base,exponent,10)
