class Solution:
    def printRightTriangle(self, n):
        # code here
        for i in range(1, n + 1):
            row_numbers = []
            for j in range(1, i + 1):
                row_numbers.append(str(j))
            print(" ".join(row_numbers))
