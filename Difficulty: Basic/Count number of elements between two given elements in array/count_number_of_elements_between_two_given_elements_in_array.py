class Solution:
    def getCount(self, arr, num1, num2):
        #Your code goes here
        a = arr.index(num1)
        b = len(arr) - 1 - arr[::-1].index(num2)
        if a > b:
            return 0
        return b - a - 1
