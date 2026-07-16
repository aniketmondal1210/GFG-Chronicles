class Solution:
    def rotateclockwise(self, arr, k):
        # code here
        n = len(arr)
        if n == 0:
            return arr
        k = k % n
        if k == 0:
            return arr
        rotated = arr[-k:] + arr[:-k]
        for i in range(n):
            arr[i] = rotated[i]
