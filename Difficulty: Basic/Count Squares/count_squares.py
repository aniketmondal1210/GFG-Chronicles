#User function Template for python3
import math
class Solution:
    def countSquares(self, n):
        # code here 
        count = 0
        i = 1
        while(i**2 < n):
            count += 1
            i += 1
        return count
