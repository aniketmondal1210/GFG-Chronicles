class Solution:
    def printDivisors(self, n):
        #code here
        result = []
        for i in range(1,n+1):
            if n % i == 0:
                result.append(i)
        return result
