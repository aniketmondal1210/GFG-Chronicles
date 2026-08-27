class Solution:
    def isTidy(self, n: int) -> bool:
        # code here
        s = str(n)
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                return False
        return True
