#User function Template for python3
import math
class Solution:
    def findArea(self,A,B,C):
        #code here
        if A + B <= C or A + C <= B or B + C <= A:
            return 0.0
        s = (A + B + C) / 2
        area = (s * (s - A) * (s - B) * (s - C)) ** 0.5
        return round(area, 3)
