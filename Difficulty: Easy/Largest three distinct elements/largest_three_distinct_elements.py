class Solution:
    def getThreeLargest(self, arr):
        # code here
        new_arr = list(set(arr))
        new_arr.sort(reverse = True)
        return new_arr[:3]
