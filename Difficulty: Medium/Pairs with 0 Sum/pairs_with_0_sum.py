class Solution:
    def getPairs(self, arr):
        # code here
        seen = set()
        result = set()
        for x in arr:
            if -x in seen:
                result.add((min(x, -x), max(x, -x)))
            seen.add(x)
        return sorted(result)
