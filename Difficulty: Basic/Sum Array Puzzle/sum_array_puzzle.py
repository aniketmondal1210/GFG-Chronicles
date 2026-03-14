class Solution:
    def sumArray(self, arr):
        #Your Code goes here
        summ = sum(arr)
        for i in range(len(arr)):
            arr[i] = summ - arr[i]
        return arr
