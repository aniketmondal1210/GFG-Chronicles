#User function Template for python3
class Solution:
    def isDisarium(self, N):
        # code here 
        summ = 0
        j = 1
        for i in str(N):
            summ += int(i)**j
            j += 1
        return 1 if summ == N else 0
