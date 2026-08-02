import math
class Solution:
    def average(self, a, b):
        """code here"""
        runs = sum(a)
        out = b.count("out")
        if out == 0:
            return -1
        return math.ceil(runs/out)
