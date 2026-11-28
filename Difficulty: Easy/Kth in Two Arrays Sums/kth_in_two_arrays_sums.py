class Solution:
    def kthItem(self, a, b, k):
        # code here
        sums = set()
        for x in a:
            for y in b:
                sums.add(x + y)
        if len(sums) < k:
            return -1
        return sorted(sums)[k - 1]
