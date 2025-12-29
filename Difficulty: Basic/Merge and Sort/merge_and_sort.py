class Solution:
    def mergeNsort(self, arr1, arr2):
        # code here
        arr = arr1 + arr2
        arr = list(set(arr))
        arr.sort()
        return arr
