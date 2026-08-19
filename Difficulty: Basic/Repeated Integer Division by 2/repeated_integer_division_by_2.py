class Solution:
    def mthHalf(self, n: int, m: int) -> int:
        # code here
        count = 0
        while count != m - 1:
            n //= 2
            count += 1
        return n  
