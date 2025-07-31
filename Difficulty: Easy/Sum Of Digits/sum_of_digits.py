class Solution:
    def sumOfDigits(self, n):
        # code here
        a = str(n)
        summ = 0
        for i in a:
            summ += int(i)
        return summ
