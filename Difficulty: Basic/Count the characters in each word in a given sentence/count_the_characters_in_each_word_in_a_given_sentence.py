#User function Template for python3
class Solution:
    def countChars(self,s):
        # code here 
        result = []
        words = s.split()
        for i in words:
            result.append(len(i))
        return result
