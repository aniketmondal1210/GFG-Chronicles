# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        return all(char in ['0','1'] for char in s)
