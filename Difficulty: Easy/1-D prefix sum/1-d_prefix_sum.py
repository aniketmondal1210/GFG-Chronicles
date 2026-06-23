class Solution:
    def prefSum(self, arr):
        # code here
        result = []
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            result.append(summ)
        return result
