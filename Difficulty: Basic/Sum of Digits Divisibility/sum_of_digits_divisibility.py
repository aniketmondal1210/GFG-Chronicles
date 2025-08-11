#User function Template for python3
class Solution:
    def isDivisible(self,N):
        #code here
        result = 0
        for i in str(N):
            result += int(i)
        return 1 if N % result == 0 else 0
