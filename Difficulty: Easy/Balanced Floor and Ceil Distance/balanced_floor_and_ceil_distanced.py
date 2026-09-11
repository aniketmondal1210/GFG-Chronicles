class Solution:
    def isBalanced(self, arr: list[int], x: int) -> bool:
        # code here
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        i = left
        if i < len(arr) and arr[i] == x:
            return True
        if i == 0 or i == len(arr):
            return False
        return (x - arr[i-1]) == (arr[i] - x)
