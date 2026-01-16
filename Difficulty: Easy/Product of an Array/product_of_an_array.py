class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        prod = 1
        for i in arr:
            prod *= i
        return prod % 1000000007
