class Solution:
    def findFinger(self, n):
        # code here
        rem = n % 8
        if rem == 1: return 1
        if rem == 2: return 2
        if rem == 3: return 3
        if rem == 4: return 4
        if rem == 5: return 5
        if rem == 6: return 4
        if rem == 7: return 3
        return 2
