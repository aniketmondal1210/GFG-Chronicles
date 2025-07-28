#User function Template for python3
class Solution:
    def isDivisible999(self, N):
        # code here
        if int(N) % 999 == 0:
            return "Divisible"
        else:
            return "Not divisible"
