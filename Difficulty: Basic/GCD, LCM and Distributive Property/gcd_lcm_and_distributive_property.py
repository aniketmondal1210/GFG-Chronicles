#User function Template for python3
import math
class Solution:
    def findValue (self, x, y, z):
        #complete the function here
        return math.gcd(math.lcm(x, y), math.lcm(x, z))
