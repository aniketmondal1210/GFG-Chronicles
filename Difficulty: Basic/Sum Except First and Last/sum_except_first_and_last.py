class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        #code here
        return sum(arr[1:len(arr)-1])
