# User function Template for python3
class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equalSum(self,arr):
        # Your code here
        total_sum = sum(arr)
        left_sum = 0
        for i in range(len(arr)):
            right_sum = total_sum - left_sum - arr[i]
            if left_sum == right_sum:
                return i
            left_sum += arr[i]
        return -1
