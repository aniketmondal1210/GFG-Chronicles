class Solution:
    def isPowerofTwo(self, n):
        # code here
        return n.bit_count() == 1
