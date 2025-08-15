#User function Template for python3
class Solution:
    def isPowerof3 (ob,N):
        # code here 
        while(N%3==0):
            N//=3
        return "Yes" if N == 1 else "No"
