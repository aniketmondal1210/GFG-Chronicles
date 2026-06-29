class Solution:
    def modify(self, N):
        #code here
        s = str(N)
        if not s:
            return 0
        result = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result.append(s[i])
        return int("".join(result))
