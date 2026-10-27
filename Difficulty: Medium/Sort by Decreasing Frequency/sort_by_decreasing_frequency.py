from collections import Counter
class Solution:
    def sortByFreq(self, arr: list[int]) -> list[int]:
        # code here
        a = Counter(arr)
        result = sorted(arr, key=lambda x: (-a[x], x))
        return result
