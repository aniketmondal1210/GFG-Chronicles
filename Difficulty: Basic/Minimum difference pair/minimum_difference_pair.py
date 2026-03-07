#User function Template for python3
class Solution:
	def minimumDifference(self, arr):
		# Code here
		arr.sort()
		mini = float('inf')
		for i in range(len(arr)-1):
		    mini = min(mini,abs(arr[i]-arr[i+1]))
		return mini
