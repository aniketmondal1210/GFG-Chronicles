#User function Template for python3
class Solution:
    def sumOfFifthPowers(self,N):
        #code here
        summ = 0
        for i in range(1,N+1):
            summ += i**5
        return summ
