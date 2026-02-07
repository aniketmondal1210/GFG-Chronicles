class Solution:
    def rearrange(self, arr):
        # code here
        result = [-1] * len(arr)
        for num in arr:
            if 0 <= num < len(arr):
                result[num] = num
        return result
