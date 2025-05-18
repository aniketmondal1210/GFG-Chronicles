#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	num_of_zeros = arr.count(0)
    	arr[:] = [num for num in arr if num != 0]
    	arr += [0]*num_of_zeros
    	return arr

# {
  # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
