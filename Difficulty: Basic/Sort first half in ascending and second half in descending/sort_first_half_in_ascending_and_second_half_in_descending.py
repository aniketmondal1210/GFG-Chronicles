#User function Template for python3
class Solution:
    def customSort(self, arr):
        # code here
        mid = len(arr)//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]
        arr1.sort()
        arr2.sort(reverse=True)
        return arr1 + arr2
