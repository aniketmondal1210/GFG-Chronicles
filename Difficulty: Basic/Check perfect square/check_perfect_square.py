#User function Template for python3
import math
class Solution:
    def checkPerfectSquare(ob, N):
        # code here
        root = math.isqrt(N)
        return "1" if root * root == N else "0"
