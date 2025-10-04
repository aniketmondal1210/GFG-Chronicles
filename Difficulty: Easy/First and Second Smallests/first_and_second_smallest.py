class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        if len(set(arr)) > 1:
            new_arr = list(set(arr))
            new_arr.sort()
            return [new_arr[0],new_arr[1]]
        else:
            return [-1]
