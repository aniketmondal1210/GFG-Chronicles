#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        result = []
        for i in b:
            result.append(i)
        for j in a:
            result.append(j)
        result.sort()
        a = len(result)
        if a % 2 == 0:
            return (result[a//2] + result[a//2-1])/2
        else:
            return result[(a-1)//2]
