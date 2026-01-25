from typing import List
class Solution:
    def findClosest(self, arr, k):
        # code here
        left, right = 0,len(arr)-1
        while(left <= right):
            mid = (left + right)//2
            if arr[mid] == k:
                return arr[mid]
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
                
        if right < 0:
            return arr[0]
        if left >= len(arr):
            return arr[len(arr) - 1]
                
        if abs(k - arr[left]) > abs(k - arr[right]):
            return arr[right]
        return arr[left]
