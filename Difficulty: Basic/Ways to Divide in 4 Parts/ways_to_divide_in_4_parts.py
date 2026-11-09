class Solution:
    def countWays(self, n):
        # code here
        if n < 4:
            return 0
        count = 0
        for a in range(1, n):
            for b in range(a, n - a - 1):
                for c in range(b, n - a - b):
                    d = n - a - b - c
                    if d >= c and d > 0:
                        count += 1
        return count
