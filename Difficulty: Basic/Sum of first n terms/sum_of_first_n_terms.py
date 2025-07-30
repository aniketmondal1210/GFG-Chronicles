#User function Template for python3
class Solution:
    def sumOfSeries(self,n):
        #code here
        summ = 0
        for i in range(1,n+1):
            summ += i**3
        return summ
