#User function Template for python3
import math
class Solution:
    def isSquare(self, S): 
        #code here
        sum = 0
        for i in S:
            if i.isalpha():
                sum += ord(i)
        sqrt = math.sqrt(sum)
        if sqrt == int(sqrt):
            return 1
        return 0
