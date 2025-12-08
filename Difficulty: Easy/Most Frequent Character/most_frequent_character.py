from collections import Counter

class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        b = list(s)
        a = Counter(b)
        freq = float('-inf')
        high_key = ''
        for key, value in a.items():
            if value > freq or (value == freq and key < high_key):
                freq = value
                high_key = key
        return high_key
