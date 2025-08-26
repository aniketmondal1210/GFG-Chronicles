#User function Template for python3
class Solution:
    def Count(self, S):
        # code here
        count = 0
        for i in S:
            if i.isalpha():
                count += 1
        return count
