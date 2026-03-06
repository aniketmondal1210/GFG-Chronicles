#User function Template for python3
from collections import Counter
class Solution:
    def countWords(self,List, n):
        #code here
        a = Counter(List)
        count = 0
        for key,value in a.items():
            if value == 2:
                count += 1
        return count
