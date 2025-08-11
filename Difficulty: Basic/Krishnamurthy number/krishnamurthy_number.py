#User function Template for python3
class Solution:
    def isKrishnamurthy(self, N):
        # code here
        result = 0
        for i in str(N):
            result += factorial(int(i))
        return "YES" if result == N else "NO"
        
        
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
