class Solution:
    def powerSet(self, s):
       #code here
       result = [""]
       for i in s:
           for j in range(len(result)):
               result.append(result[j] + i)
       return sorted(result)
