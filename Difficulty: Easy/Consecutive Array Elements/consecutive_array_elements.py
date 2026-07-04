class Solution:
    def areConsecutives(self, arr):
        # code here
        if not arr:
            return False
        mini = min(arr)
        maxi = max(arr)
        if maxi - mini + 1 != len(arr):
            return False
        return len(set(arr)) == len(arr)
