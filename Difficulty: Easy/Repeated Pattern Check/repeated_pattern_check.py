class Solution:
    def findPattern(self, s):
        # code here
        x_count = 0
        y_count = 0
        for i in range(len(s)):
             if s[i] == 'x':
                  x_count += 1
             elif s[i] == 'y':
                  y_count += 1
             if (i == len(s)-1) or (s[i] == 'y' and s[i+1] == 'x'):
                  if x_count != y_count:
                       return False
        return True
