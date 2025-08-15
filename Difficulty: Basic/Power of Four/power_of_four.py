# you may use python module's
# just return true/false or 1/0
class Solution():
    def isPowerofFour(self, n):
         # code here
        while(n%4==0):
             n//=4
        return n == 1
