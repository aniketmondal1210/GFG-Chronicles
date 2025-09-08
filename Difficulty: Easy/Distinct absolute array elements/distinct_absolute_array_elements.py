class Solution:
    def distinctCount(self, arr):
        #Your code goes here.
            result = []
            for i in arr:
               result.append(abs(i))
            return len(set(result))
