#User function Template for python3
class Solution:
    def theLastDigit (self,a,b,c,d,e,f):
        # code here 
        x = pow(a, b, 10)
        y = pow(c, d, 10)
        z = pow(e, f, 10)
        ans = (x * y * z) % 10
        return ans
