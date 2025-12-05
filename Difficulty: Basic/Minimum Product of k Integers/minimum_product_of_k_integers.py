#User function Template for python3
class Solution:
    def minProduct(self, arr, k):
        # code here
        arr.sort()
        new_arr = arr[:k]
        prod = 1
        for num in new_arr:
            prod = (prod * num) % (10**9 + 7)
        return prod
