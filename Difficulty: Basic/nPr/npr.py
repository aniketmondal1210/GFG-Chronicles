#User function Template for python3

class Solution:
    def nPr(self, n, r):
        # code here
        if r > n:
            return 0
        else:
            return fact(n)//fact(n-r)
        
    
    
def fact(x):
    if x <= 1:
        return 1
    else:
        prod = 1
        for i in range(2,x+1):
            prod *= i
        return prod
