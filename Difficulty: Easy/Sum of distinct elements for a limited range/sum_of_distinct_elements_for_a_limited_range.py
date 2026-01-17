class Solution:
    # Function to calculate the sum of distinct elements in the array.
    def sumOfDistinct(self, arr):
        # Your code goes here
        a = set(arr)
        return sum(a)
