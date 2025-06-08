#User function Template for python3
from itertools import combinations
class Solution:
    def subsets(self, arr):
        # code here
        result = []
        for i in range(len(arr)+1):
            for subset in combinations(arr,i):
                result.append(subset)
        return sorted(result)
