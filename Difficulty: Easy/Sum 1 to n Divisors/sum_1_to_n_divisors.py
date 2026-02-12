class Solution:
    def sumOfDivisors(self, n):
        # code here
        total = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    total += j
        return total
