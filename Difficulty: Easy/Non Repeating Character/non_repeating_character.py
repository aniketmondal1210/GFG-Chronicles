from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        a = Counter(s)
        for key,value in a.items():
            if value == 1:
                return key
        return '$'
