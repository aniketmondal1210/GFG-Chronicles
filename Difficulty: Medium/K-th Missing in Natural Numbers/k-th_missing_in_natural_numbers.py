class Solution:
    def findKthSmall(self, arr, k):
        # code here
        arr_set = set(arr)
        remaining = []
        num = 1
        while len(remaining) < k:
            if num not in arr_set:
                remaining.append(num)
            num += 1
        return remaining[k - 1]
