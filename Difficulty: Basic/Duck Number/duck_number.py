#User function Template for python3
class Solution:
    def check_duck(self, N):
        # code here
        if N == '0':
            return False
        elif N[0] == '0':
            return False
        elif '0' in N[1:]:
            return True
        return False
