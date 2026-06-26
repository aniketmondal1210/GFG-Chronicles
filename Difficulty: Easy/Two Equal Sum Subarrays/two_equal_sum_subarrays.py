class Solution:
    def canSplit(self, arr):
        #code here
        summ = sum(arr)
        if summ % 2 != 0:
            return False
        target = summ // 2
        curr_sum = 0
        for i in range(len(arr) - 1):
            curr_sum += arr[i]
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
        return False
