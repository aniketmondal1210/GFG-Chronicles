import math
class Solution:
    def isPerfect(self,N):
        #code here
        summ = 0
        for i in str(N):
            summ += math.factorial(int(i))
        return 1 if summ == N else 0
