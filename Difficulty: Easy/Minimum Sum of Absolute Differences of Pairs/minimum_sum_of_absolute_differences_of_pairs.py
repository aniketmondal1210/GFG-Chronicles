#User function Template for python3
class Solution:
    def findMinSum(self, A, B, N):
        if len(A) != len(B):
            raise ValueError("Input arrays A and B must be of equal length")
        
        A.sort()
        B.sort()
        summ = 0
        for i in range(N):
            summ += abs(A[i] - B[i])
        return summ
