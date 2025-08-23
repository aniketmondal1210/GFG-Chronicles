class Solution:
    def gcd(self, a, b):
        # code here
        while b != 0:
            a,b = b, a % b
        return a


'''
***Dont' Use***
import math
class Solution:
    def gcd(self, a, b):
        # code here
        return math.gcd(a,b)'''
