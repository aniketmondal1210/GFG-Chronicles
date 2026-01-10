#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        a = Counter(arr)
        for key,value in a.items():
            if value == 1:
                return key
        return 0
