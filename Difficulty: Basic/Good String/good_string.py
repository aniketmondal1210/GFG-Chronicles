class Solution:
    def isGoodString(self, s: str) -> bool:
        # code here.
        if len(s) <= 1:
            return True
        for i in range(len(s) - 1):
            c1 = s[i]
            c2 = s[i + 1]
            diff = abs(ord(c1) - ord(c2))
            cyclic_dist = min(diff, 26 - diff)
            if cyclic_dist != 1:
                return False
        return True
