#User function Template for python3
class Solution:
    def isStrong(self, N):
        # code here 
        summ = 0
        for i in str(N):
            summ += fact(int(i))
        return "1" if summ == N else "0"
        
def fact(x):
    if x <= 1:
        return 1
    return x*fact(x-1)
