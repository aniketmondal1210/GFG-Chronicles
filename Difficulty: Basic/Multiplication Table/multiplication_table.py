#User function Template for python3
class Solution:
    def getTable(self,n):
        # code here
        result = []
        for i in range(1,11):
            result.append(n*i)
        return result
