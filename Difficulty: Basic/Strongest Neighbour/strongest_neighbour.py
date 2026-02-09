class Solution:
    def maxAdj(self, arr):
        # code here
        result = []
        for i in range(len(arr)-1):
            result.append(max(arr[i],arr[i+1]))
        return result
