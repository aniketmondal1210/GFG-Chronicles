class Solution:
    def maxTripletSum(self, arr): 
        # Code Here
        arr.sort()
        return arr[-1] + arr[-2] + arr[-3]
