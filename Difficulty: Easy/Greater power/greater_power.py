#User function Template for python3
import math
class Solution:
    def greaterPower(self, a , b , m , n):
        # code here 
        e = b * math.log(a)
        f = n * math.log(m)
        if e > f:
            return 1
        elif e == f:
            return -1
        else:
            return 0
