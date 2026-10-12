class Solution:
    def pairWiseConsecutive(self, st: list[int]) -> bool:
        # code here
        start = len(st) - 2 if len(st) % 2 != 0 else len(st) - 1
        for i in range(start, 0, -2):
            if abs(st[i] - st[i-1]) != 1:
                return False
        return True
