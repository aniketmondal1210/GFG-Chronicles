class Solution:
    def countZeroes(self, A, N):
        count = 0
        for i in A:
            for j in i:
                if j == 0:
                    count += 1
        return count
