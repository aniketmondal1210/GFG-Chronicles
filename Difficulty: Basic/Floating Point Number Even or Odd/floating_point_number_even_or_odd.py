class Solution:
    def isEven(self, s):
        # code here
        dot = s.find('.')
        if dot == -1:
            return int(s[-1]) % 2 == 0
        frac = s[dot + 1:].rstrip('0')
        if not frac:
            return int(s[dot - 1]) % 2 == 0
        return int(frac[-1]) % 2 == 0
