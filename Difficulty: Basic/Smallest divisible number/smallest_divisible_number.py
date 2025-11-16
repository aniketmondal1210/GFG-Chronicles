import math
class Solution:
    def getSmallestDivNum(self, n): 
        # code here 
        result = 1
        for i in range(1,n+1):
            result = math.lcm(result,i)
        return result
