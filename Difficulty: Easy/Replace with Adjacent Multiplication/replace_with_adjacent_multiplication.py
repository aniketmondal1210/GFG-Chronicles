class Solution:
    def updateArray(self, arr):
        # code here
        n = len(arr)
        if n <= 1:
            return arr
        result = [arr[0] * arr[1]]
        for i in range(1, n - 1):
            a = arr[i-1] * arr[i] * arr[i+1]
            result.append(a)
        result.append(arr[-2] * arr[-1])
        for j in range(n):
            arr[j] = result[j]
        return arr
