#User function Template for python3
import math
class Solution:
    def gcd(self, n, arr):
        # code here
        arr.sort()
        num = arr[0]
        for i in arr:
            num = math.gcd(num,i)
        return num
