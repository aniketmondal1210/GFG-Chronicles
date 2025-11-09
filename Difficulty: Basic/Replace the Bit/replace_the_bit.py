#User function Template for python3
class Solution:
    def replaceBit(self, N, K):
        # code here
        a = bin(N)[2:]
        if len(a) < K:
            return N
        if a[K-1] == '1':
            a = a[:K-1] + '0' + a[K:]
            return int(a, 2)
        return N
