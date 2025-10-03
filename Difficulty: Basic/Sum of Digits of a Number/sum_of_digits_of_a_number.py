class Solution:
    def sumOfDigits(self, n):
        # code here
        result = 0
        for i in str(n):
            result += int(i)
        return result
