class Solution:
    def reverseexponentiation(self, n):
        # code here
        a = int(str(n)[::-1])
        return n**a
