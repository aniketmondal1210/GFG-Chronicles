#User function Template for python3
class Solution:
    def bitMultiply(self, N):
        # code (here
        a = bin(N)[2:]
        b = a.count('1')
        return N*b
