#User function Template for python3
class Solution:
    def evenFactors (self, N):
        # code here
        summ = 0
        for i in range(1,N+1):
            if i % 2 == 0 and N % i == 0:
                summ += i
        return summ
