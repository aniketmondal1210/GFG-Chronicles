class Solution:
    def calculateFriendliness(self, arr):
        # code here
        result = abs(arr[0] - arr[-1])
        for i in range(len(arr)-1):
            result += abs(arr[i] - arr[i+1])
        return result
