#User function Template for python3
class Solution:
    def mulClock(self, num1, num2):
        # code here
        if num1*num2 < 12:
            return num1*num2
        else:
            return (num1*num2)%12
