class Solution: 
    def extraChar(self,s1, s2):
        # code here
        result = 0
        for i in s1:
            result ^= ord(i)
        for j in s2:
            result ^= ord(j)
        return chr(result)
