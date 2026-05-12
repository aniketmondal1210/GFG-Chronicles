class Solution:
    def rowWithMax1s(self, arr):
        # code here
        maxi = 0
        idx = -1
        for i in range(len(arr)):
            count = arr[i].count(1)
            if count > maxi:
                maxi = count
                idx = i
        return idx
