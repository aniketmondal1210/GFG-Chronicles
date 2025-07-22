#User function Template for python3
import math
#User function Template for python3
class Solution:
    def isPerfectSquare (self, n):
        # code here 
        sqrt = math.sqrt(n)
        if int(sqrt) == sqrt:
            return 1
        return 0
