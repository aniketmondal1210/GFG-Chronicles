class Solution:
    def closestNumber(self, n, m):
        # code here 
        q = n // m
        x = m * q
        y = m * (q + 1)
        if abs(n - x) < abs(n - y):
            return x
        elif abs(n - x) > abs(n - y):
            return y
        else:
            return x if abs(x) > abs(y) else y
