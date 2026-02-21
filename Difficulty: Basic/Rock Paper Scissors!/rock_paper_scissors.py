#User function Template for python3
class Solution:
    def gameResult(self, s):
        # code here
        if s[0] == s[-1]:
            return "DRAW"
        elif (s[0] == 'R' and s[-1] == 'S') or (s[0] == 'S' and s[-1] == 'P') or (s[0] == 'P' and s[-1] == 'R'):
            return "A"
        else:
            return "B"
