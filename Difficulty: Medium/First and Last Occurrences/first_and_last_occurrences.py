#User function Template for python3
class Solution:
    def find(self, arr, x):
        # code here
        result = []
        for i in range(len(arr)):
            if arr[i] == x:
                result.append(i)
        if not result:
            return [-1, -1]
        return [result[0], result[-1]]
