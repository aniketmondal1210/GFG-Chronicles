#User function Template for python3
class Solution:
    def checkYear (self, n):
        # code here
        if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
            return True
        return False
