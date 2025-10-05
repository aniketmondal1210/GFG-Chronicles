#User function Template for python3
class Solution:
    def changeBase(self, N ,K):
        # code here 
        result = ""
        while(N > 0):
            digit = N % K
            result += str(digit)
            N //= K
        return result[::-1]
