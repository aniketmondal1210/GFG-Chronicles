class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        return all(arr[i]<=arr[i+1] for i in range(len(arr)-1))
