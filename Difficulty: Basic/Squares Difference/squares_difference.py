#User function Template for python3
class Solution:
    def squaresDiff (self, N):
        # code here 
        a = (N*(N+1)*(2*N+1))//6
        b = N*(N+1)//2
        return abs(a - b**2)
