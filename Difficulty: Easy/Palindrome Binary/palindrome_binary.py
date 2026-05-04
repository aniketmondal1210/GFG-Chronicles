class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        a = bin(n)[2:]
        if a == a[::-1]:
            return 1
        return 0
