#User function Template for python3
#Back-end complete function Template for Python 3
class Solution:
    # Prints average of a prefix array
    def prefixAvg(self, arr):
        result = []
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            result.append(total // (i + 1))
        return result
