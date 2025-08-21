#User function Template for python3
class Solution:
	def findMaximum(self, arr):
		# code here
		for i in range(len(arr)-1):
		    if arr[i] <= arr[i+1]:
		        continue
		    else:
		        return arr[i]
