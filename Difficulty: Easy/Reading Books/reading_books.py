class Solution:
    def maxPoint(self, k, arr1, arr2):
        #code here
        maxi = 0
        for i in range(len(arr1)):
            times = k // arr1[i]
            points = times * arr2[i]
            if points > maxi:
                maxi = points
        return maxi
