class Solution:
    def getNthPell(self, n):
        # Code here
        MOD = 10**9 + 7
        if n == 0:
            return 0
        if n == 1:
            return 1
        p0, p1 = 0, 1
        for i in range(2, n + 1):
            p0, p1 = p1, (2 * p1 + p0) % MOD
        return p1
