class Solution:
    def MaximumIntegerValue(self,S):
        #code here
        result = int(S[0])
        for i in range(1, len(S)):
            digit = int(S[i])
            result = max(result + digit, result * digit)
        return result
