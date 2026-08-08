class Solution:
    def sumOfSubsets(self, n: int) -> int:
        # code here
        if n == 0:
            return 0
        sum_n = n * (n + 1) // 2
        occurrences = pow(2, n - 1)
        return sum_n * occurrences
