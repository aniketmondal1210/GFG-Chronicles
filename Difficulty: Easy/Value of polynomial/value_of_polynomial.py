class Solution:
    def evaluatePoly(self, poly, x):
        # code here 
        summ = 0
        n = len(poly)
        for i in range(n):
            power = n - 1 - i
            summ += poly[i]*(x ** power)
        return summ
