class Solution:
    def checkIsAP(self, arr):
        #Your code goes here
        arr.sort()
        d = arr[1]-arr[0]
        flag = True
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != d:
                flag = False
                break
        return flag
