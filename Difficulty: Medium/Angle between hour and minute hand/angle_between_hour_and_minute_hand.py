class Solution:
    def getAngle(self, s: str) -> float:
        #code here
        if len(s) == 5:
            h = int(s[:2])
            m = int(s[3:])
        else:
            h = int(s[0])
            m = int(s[2:])
        h %= 12
        a = abs(30 * h - 5.5 * m)
        return min(a, 360 - a)
