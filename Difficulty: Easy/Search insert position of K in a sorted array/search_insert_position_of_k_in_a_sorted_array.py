class Solution:
    def searchInsertK(self, arr, k):
        # code here
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return start
