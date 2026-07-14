class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        result = []
        n = len(arr)
        for i in range(n // 2):
            result.append(arr[n - 1 - i])
            result.append(arr[i])
        if n % 2 != 0:
            result.append(arr[n // 2])
        return result
