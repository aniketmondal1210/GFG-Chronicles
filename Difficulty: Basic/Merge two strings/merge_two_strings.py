#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        result = ''
        for i in range(max(len(S1),len(S2))):
            if i < len(S1):
                result += S1[i]
            if i < len(S2):
                result += S2[i]
        return result
