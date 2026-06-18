class Solution:
    def max_happiness(self, arr):
        # code here
        maxi = arr[0] + arr[1]
        for i in range(1, len(arr) - 1):
            curr = arr[i] + arr[i + 1]
            if curr > maxi:
                maxi = curr
        return maxi
