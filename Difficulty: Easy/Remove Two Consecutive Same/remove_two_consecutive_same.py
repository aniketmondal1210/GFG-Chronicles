class Solution:
    def removeConsecutiveSame(self, arr):
        # code here
        result = []
        for i in range(len(arr)):
            if result and (result[-1] == arr[i]):
                result.pop()
            else:
                result.append(arr[i])
        return len(result)
