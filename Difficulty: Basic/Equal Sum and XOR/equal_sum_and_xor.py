class Solution:
    def countValues(self, n):
        # code here
        count = 0
        for i in range(n+1):
            if n + i == n ^ i:
                count += 1
        return count
