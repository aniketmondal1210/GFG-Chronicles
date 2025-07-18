#User function Template for python3
class Solution:
    def altProduct(self, arr):
       # Your code goes here
        arr.sort()
        mid = len(arr)//2
        sum = 0
        for i in range(mid):
            sum += arr[i]*arr[len(arr)-i-1]
        return sum
