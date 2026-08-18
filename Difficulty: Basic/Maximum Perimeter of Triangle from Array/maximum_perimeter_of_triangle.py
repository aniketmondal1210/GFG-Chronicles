class Solution:
    def maxPerimeter(self, arr):
        #code here.
        arr.sort(reverse=True)
        for i in range(len(arr) - 2):
            if arr[i+1] + arr[i+2] > arr[i]:
                return arr[i] + arr[i+1] + arr[i+2]
        return -1
