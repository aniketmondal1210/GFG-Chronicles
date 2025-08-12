class Solution:
    def nCr(self, n, r):
        # code here
        if n < r:
            return 0
        else:
            return fact(n) // (fact(r)*fact(n-r))

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
