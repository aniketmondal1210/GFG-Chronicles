#User function Template for python3
class Solution:
    def DivisibleByEight(self,s):
        #code here
        if int(s[-3:]) % 8 == 0:
            return 1
        return -1
