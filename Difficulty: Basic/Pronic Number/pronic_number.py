class Solution:
    def pronicNumbers(self, n):
        # code here
        result = []
        i = 0
        while i*(i+1) <= n:
            result.append(i * (i + 1))
            i += 1
        return result
