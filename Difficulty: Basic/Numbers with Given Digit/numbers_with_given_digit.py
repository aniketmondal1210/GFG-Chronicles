class Solution:
    def findNumbers(self, n, d):
        # code here
        result = []
        target = str(d)
        for i in range(n + 1):
            if target in str(i):
                result.append(i)
        return result
