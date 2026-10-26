class Solution:
    def countElements(self, arr):
        # code here
        return (max(arr) - min(arr) + 1) - len(set(arr))
