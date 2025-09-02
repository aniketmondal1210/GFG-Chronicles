import math
class Solution:
    def divFloorCeil(self, a, b):
        # code here
        floor_div = math.floor(a/b)
        ceil_div = math.ceil(a/b)
        return [floor_div, ceil_div]
