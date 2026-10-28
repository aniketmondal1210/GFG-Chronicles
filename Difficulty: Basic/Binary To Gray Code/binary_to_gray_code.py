class Solution:
    def binaryToGray(self, n):
        # code here
        return n ^ (n >> 1)
