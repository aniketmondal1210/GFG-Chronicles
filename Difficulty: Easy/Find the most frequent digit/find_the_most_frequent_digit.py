#User function Template for python3
from collections import Counter
class Solution:
    def solve(self, N):
        # code here
        result = [int(i) for i in N]
        a = Counter(result)
        b = max(a.values())
        array = []
        for key,value in a.items():
            if value == b:
                array.append(key)
        return max(array)
