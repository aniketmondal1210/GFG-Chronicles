class Solution:
    def solve(self, n, s):
        # code here
        occupied = set()
        rejected = 0
        seen = set()
        for i in s:
            if i not in seen:
                seen.add(i)
                if len(occupied) < n:
                    occupied.add(i)
                else:
                    rejected += 1
            else:
                if i in occupied:
                    occupied.remove(i)
        return rejected
