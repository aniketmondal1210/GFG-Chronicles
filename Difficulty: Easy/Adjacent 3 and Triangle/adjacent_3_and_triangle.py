class Solution:
    def canMakeTriangle(self, arr):
        # code here
        result = []
        n = len(arr)
        for i in range(n - 2):
            a = arr[i]
            b = arr[i+1]
            c = arr[i+2]
            if (a + b > c) and (a + c > b) and (b + c > a):
                result.append(1)
            else:
                result.append(0)
        return result
