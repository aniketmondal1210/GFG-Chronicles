#User function Template for python3
import math
class Solution:
    def getCompundInterest(self, P ,T , N , R):
        # code here
        future_value = P * (1 + (R/100)/N)**(N*T)
        return math.floor(future_value)
