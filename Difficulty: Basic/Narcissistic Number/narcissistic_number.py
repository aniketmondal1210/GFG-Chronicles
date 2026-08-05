class Solution:
    def isNarcissistic(self, n):
        # Code here
        digits = [int(i) for i in str(n)]
        length = len(str(n))
        summ = 0
        for i in digits:
            summ += i**length
        return summ == n
