class Solution:
    def getMinMax(self, arr):
        # code here
        mini = float('inf')
        maxi = float('-inf')
        for i in arr:
            if i < mini:
                mini = i
            if i > maxi:
                maxi = i
        return [mini, maxi]
