#User function Template for python3
class Solution:
    def is_common(self, s, t):
        # Code here
        if len(set(s).intersection(set(t))) != 0:
            return "CHANGE"
        return "BEHAPPY"
