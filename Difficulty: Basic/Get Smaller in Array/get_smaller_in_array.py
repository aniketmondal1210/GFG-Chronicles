class Solution:
    def getSmaller(self, arr, target):
        # code here
        result = []
        for i in arr:
            if target > i:
                result.append(i)
        return result
