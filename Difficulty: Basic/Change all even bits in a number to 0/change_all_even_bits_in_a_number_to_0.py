#User function Template for python3
class Solution:
    def convertEvenBitToZero (ob, n):
        # code here 
        a = (bin(n)[2:])[::-1]
        b = ''
        for i in range(len(a)):
            if i % 2 == 0:
                b += '0'
            else:
                b += a[i]
        b = b[::-1]
        return int(b,2)
