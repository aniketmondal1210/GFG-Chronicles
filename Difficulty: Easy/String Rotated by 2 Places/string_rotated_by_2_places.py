class Solution:
    def isRotated(self,s1,s2):
        #code here
        if len(s1) != len(s2):
            return False
        if len(s1) == 2:
            return s1 == s2
        anticlock = s1[2:] + s1[:2]
        clock = s1[-2:] + s1[:-2]
        return s2 == anticlock or s2 == clock
