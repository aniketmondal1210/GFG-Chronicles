#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        result = []
        for bit in S:
            if bit == '1':
                result.append('0')
            else:
                result.append('1')
        return ''.join(result)
