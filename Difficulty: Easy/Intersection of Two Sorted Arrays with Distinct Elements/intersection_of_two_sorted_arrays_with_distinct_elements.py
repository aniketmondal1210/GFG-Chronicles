#User function Template for python3
class Solution:
    def intersection(self, a, b):
        # Your code here
        a = list(set(a).intersection(set(b)))
        return sorted(a)
