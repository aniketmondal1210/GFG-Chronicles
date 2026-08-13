from collections import Counter
class Solution:
    def maximumFrequency(self, s):
        # Code here
        a = s.split()
        b = Counter(a)
        result = []
        c = max(b.values())
        for word in a:
            if b[word] == c:
                return f"{word} {c}"
