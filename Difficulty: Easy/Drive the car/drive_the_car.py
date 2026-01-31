#User function Template for python3
class Solution:
    # Function to calculate the difference between the maximum element in the array and a given number k
    def required(self, arr, k):
        # Your code goes here
        if max(arr) > k:
            return max(arr) - k
        return -1
