#User function Template for python3
class Solution:
    def countWrongPlacedBalls(self, s):
        # code here
        count = 0
        for i in range(len(s)):
            if i % 2 == 1 and s[i] == 'R':
                count += 1
            if i % 2 == 0 and s[i] == 'B':
                count += 1
        return count
