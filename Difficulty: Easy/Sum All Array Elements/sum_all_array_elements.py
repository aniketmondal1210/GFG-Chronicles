class Solution:
    def arraySum(self, arr):
        # code here
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
        return summ
