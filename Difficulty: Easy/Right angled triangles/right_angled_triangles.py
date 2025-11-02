#User function Template for python3
class Solution:
    def rightAngTri(self, a, b, c):
        # code here 
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
            return "Yes"
        return "No"
