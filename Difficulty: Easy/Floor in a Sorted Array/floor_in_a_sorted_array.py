class Solution:
    def findFloor(self, arr, x):
        # code here
        for i in range(len(arr)):
            if arr[i] <= x:
                continue
            else:
                return i - 1
        return len(arr) - 1
