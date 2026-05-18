class Solution:
    def minimumDifference(self, arr):
		# Code here
        arr.sort()
        mini = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff < mini:
                mini = diff
        return mini
