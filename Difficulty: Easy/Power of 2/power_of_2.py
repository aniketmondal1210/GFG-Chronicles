class Solution:
    def isPowerofTwo(self, n):
        # code here
        return bin(n)[2:].count('1') == 1
