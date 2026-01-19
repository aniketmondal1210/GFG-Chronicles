#User function Template for python3
class Solution:
    def findMinimumIF(self, arr):
        # Your code goes here
        reversed_arr = []
        for i in arr:
            reversed_num = int(str(i)[::-1])
            reversed_arr.append(reversed_num)

        reversed_arr.sort()
        
        mini = float('inf')
        for i in range(len(reversed_arr) - 1):
            diff = abs(reversed_arr[i+1] - reversed_arr[i])
            mini = min(mini, diff)
        
        return mini
