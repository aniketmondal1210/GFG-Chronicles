#User function Template for python3
class Solution:
    def findMissing(self,a,b):
        # code here
        b_set = set(b)
        result = []
        for i in a:
            if i not in b_set:
                result.append(i)
        return result
