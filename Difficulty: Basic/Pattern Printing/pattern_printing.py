#User function Template for python3
class Solution:
    def printPattern(self, N):
        # code here
        s = ""
        for i in range(1, N + 1):
            s += ('*' * i) + " "
        print(s.strip(), end="")
