import math
class Solution:
    def totalJumps(self, arr, x, y):
        # code here
        net_up = x - y
        summ = 0
        for h in arr:
            if h <= x:
                summ += 1
            else:
                summ += math.ceil((h - x) / net_up) + 1
        return summ
