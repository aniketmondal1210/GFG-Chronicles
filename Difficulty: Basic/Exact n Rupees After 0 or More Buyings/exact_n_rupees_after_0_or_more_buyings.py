class Solution:
    def isPossible(self, n):
        # code here
        target = 100 - n
        if target < 0:
            return False
        for y in range(target//7+1):
            remainder = target - (7*y)
            if remainder % 3 == 0:
                return True
        return False
