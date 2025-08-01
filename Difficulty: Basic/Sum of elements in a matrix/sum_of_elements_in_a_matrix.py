#User function Template for python3
class Solution:
    def sumOfMatrix(self,N,M,Grid):
        #code here
        summ = 0
        for i in Grid:
            summ += sum(i)
        return summ
