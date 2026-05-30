class Solution:
    def replaceElements(self, arr):
        # code here
        if len(arr) < 2:
            return arr
        n = len(arr)
        original = arr[:]
        for i in range(n):
            if i == 0:
                arr[i] = original[i] ^ original[i+1]
            elif i == n-1:
                arr[i] = original[i-1] ^ original[i]
            else:
                arr[i] = original[i-1] ^ original[i+1]
        return arr
