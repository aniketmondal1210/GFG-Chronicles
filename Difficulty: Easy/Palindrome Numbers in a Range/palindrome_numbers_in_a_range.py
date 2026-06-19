class Solution:
    def printPalindromes(self, m, n):
        # code here
        result = []
        for i in range(m, n + 1):
            s = str(i)
            if s == s[::-1]:
                result.append(i)
        return result
