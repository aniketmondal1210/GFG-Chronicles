#User function Template for python3
class Solution:
    def subsequenceSum(self, s):
        # code here
        digits = [int(k) for k in s]
        n = len(digits)
        summ = 0
        for i in range(n):
            summ += digits[i]*(2**(n-1))
        return summ
