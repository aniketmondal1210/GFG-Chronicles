#User function Template for python3
class Solution:
    def isDivisibleBy10(self,bin):
        #code here
        a = int(bin,2)
        return 1 if a % 10 == 0 else 0
