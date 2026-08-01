class Solution:
    def dupLastIndex(self, arr):
        # Complete the function
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] == arr[i + 1]:
                return [i + 1, arr[i]]
        return [-1, -1]
