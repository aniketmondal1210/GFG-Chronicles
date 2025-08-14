#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        result = []
        for i in range(1,len(arr)+1):
            if arr[i-1] == i:
                result.append(i)
        return result
