#User function Template for python3
class Solution:
    def isPallindrome(self, N):
        # code here
        a = bin(N)[2:]
        return "1" if a[::-1] == a else "0"
