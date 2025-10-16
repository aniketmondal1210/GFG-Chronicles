#User function Template for python3
class Solution:
    def onesComplement(self,N):
        #code here
        a = bin(N)[2:]
        b = ""
        for i in a:
            if i == '1':
                b += '0'
            else:
                b += '1'
        return int(b,2)
