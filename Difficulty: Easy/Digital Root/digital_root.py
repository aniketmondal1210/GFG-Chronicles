class Solution:
    def digitalRoot(self, n: int) -> int:
        # code here
        while n >= 10:
            n = sum(int(i) for i in str(n))
        return n
