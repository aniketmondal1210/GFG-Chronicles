#User function Template for python3
class Solution:
    def binaryAdd(self, n, s):
        # code here
        # s = s[::-1] #O(n)
        s = list(s[::-1])
        carry = 1
        for i in range(n):
            if carry == 0:
                break
            if s[i] == '0':
                s[i] = '1'
                carry = 0
            else:    #s[i] == '1'
                s[i] = '0'
                carry = 1
        if  carry == 1:
            s.append('1')
        s = ''.join(s[::-1])
        return s
