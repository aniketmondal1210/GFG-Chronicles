#User function Template for python3 
class Solution: 
    def pattern(self, s): 
        # code here 
        result = []
        for i in range(len(s), 0, -1):
            result.append(s[:i])
        return result
