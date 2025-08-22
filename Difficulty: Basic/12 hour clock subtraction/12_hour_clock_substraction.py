#User function Template for python3
class Solution:
    def subClock(self, num1, num2):
        # code here
        sub = num1 - num2
        if sub >= 0:
            return sub%12
        else:
            return (12+sub)%12
