class Solution:
    def nthTerm(self, a, r, n):
        MOD = 1000000007
        return (a * r * pow(r, n-2, MOD) % MOD)
