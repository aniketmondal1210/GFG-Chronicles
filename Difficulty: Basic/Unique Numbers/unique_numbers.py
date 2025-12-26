#User function Template for python3
class Solution:
    def uniqueNumbers(self, L, R):
        # code here
        result = []
        for i in range(L, R+1):
            if len(set(str(i))) == len(str(i)):
                result.append(i)
        return result
