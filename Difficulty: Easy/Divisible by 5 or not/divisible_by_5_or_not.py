#User function Template for python3
class Solution:
    def isDivisibleBy5(self, Bin):
        # code here
        if int(Bin,2) % 5 == 0:
            return "Yes"
        else:
            return "No"
