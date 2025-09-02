import math
class Solution:
    def lcm(self, a, b):
        # code here
        return math.lcm(a,b)


OR 


class Solution:
    def hcf(self, a, b):
        if a == 0:
            return abs(b)
        if b == 0:
            return abs(a)
        while b:
            a, b = b, a % b
        return abs(a)
    
    def lcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.hcf(a, b)
