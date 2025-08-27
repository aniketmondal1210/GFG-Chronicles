#User function Template for python3
class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        a = sum(arr[:len(arr)//2])
        b = sum(arr[len(arr)//2:])
        return abs(a-b)
