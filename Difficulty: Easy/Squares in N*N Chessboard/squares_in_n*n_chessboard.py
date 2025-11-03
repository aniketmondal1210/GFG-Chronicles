#User function Template for python3
class Solution:
    def squaresInChessBoard(self, N):
         # code here
         summ = 0
         for i in range(1,N+1):
             summ += i*i
         return summ
