class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        ans = float('inf')
        for i in range(n + 1):
            t_s1 = i * s1
            t_s2 = (n - i) * s2
            ans = min(ans, max(t_s1, t_s2))
        return ans
