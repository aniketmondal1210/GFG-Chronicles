#User function Template for python3
class Solution:
    def RedOrGreen(self,N,S):
        #code here
        R_count = S.count('R')
        G_count = S.count('G')
        return min(R_count,G_count)
