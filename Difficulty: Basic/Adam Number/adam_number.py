#User function Template for python3
class Solution:
    def checkAdamOrNot(self, N):
        # code here 
        a = str(N**2)
        b = str(int(str(N)[::-1])**2)
        return "YES" if a == b[::-1] else "NO"
