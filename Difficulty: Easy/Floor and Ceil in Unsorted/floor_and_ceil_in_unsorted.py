class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floor = -1
        ceil = -1
        for i in arr:
            if i == x:
                return [x, x]
            if i < x:
                if floor == -1 or i > floor:
                    floor = i
            if i > x:
                if ceil == -1 or i < ceil:
                    ceil = i
        return [floor, ceil]
