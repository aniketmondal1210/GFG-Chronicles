class Solution:
    def termOfGP(self, a, b, n):
        # code here
        if n == 1:
            return a
        if n == 2:
            return b
        if a == 0:
            return 0
        r = b/a
        return int(a * (r ** (n - 1)))
