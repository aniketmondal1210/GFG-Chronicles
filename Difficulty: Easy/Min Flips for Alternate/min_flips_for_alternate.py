class Solution:
    def minFlips(self, s):
        # Code here
        n = len(s)
        candidate1 = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
        candidate2 = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
        flips1 = sum(1 for a, b in zip(s, candidate1) if a != b)
        flips2 = sum(1 for a, b in zip(s, candidate2) if a != b)
        return min(flips1, flips2)
