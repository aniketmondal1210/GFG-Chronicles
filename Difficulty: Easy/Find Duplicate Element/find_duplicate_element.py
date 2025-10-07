#User function Template for python3
class Solution:
    def findDuplicate(self,arr):
    # Your code goes here
        seen = set()
        for i in arr:
            if i in seen:
                return i
            seen.add(i)
