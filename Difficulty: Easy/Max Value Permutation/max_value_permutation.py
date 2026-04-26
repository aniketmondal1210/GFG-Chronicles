#User function Template for python3
class Solution:
    def maxValue(self, arr): 
        # Complete the function
        arr.sort()
        mod = 10**9 + 7
        summ = 0
        for i in range(len(arr)):
            summ += i*arr[i]
        return summ % mod
