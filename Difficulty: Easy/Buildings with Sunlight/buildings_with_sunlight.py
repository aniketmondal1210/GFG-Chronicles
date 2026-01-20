#User function Template for python3
class Solution:
    def longest(self, arr):
        #Code Here
        if not arr:
            return 0
        count = 1
        maxi = arr[0]
        for i in range(1,len(arr)):
            if arr[i] >= maxi:
                count += 1
                maxi = arr[i]
        return count
