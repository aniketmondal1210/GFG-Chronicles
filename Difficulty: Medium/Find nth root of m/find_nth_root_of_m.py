class Solution:
    def nthRoot(self, n, m):
       # code here
        if m == 0:
            return 0
        if m == 1:
            return 1
        for i in range(2, m + 1):
            result = i ** n
            if result == m:
                return i
            if result > m:
                break
        return -1
