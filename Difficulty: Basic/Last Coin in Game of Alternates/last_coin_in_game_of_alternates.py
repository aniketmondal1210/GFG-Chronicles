class Solution:
    def coin(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        while right - left > 1:
            if arr[left] >= arr[right]:
                left += 1
            else:
                right -= 1
        return min(arr[right],arr[left])
