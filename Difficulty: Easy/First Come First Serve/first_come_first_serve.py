#User function Template for python3
from collections import Counter
class Solution:
    def firstElement(self, arr, k):
        result = []
        a = Counter(arr)
        for key,value in a.items():
            if value == k:
                result.append(key)
        if len(result) == 0:
            return -1
        mini = float('inf')
        for i in result:
            mini = min(arr.index(i),mini)
        return arr[mini]
