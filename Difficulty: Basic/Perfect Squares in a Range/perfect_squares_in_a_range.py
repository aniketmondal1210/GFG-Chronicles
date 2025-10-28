#User function Template for python3
import math
class Solution:
    def numOfPerfectSquares(self, a, b):
        # code here
        count = 0
        for i in range(a, b + 1):
            root = math.isqrt(i)
            if root * root == i:
                count += 1
        return count
