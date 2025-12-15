#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		a = arr[:l-1]
		b = arr[l-1:r]
		c = arr[r:]
		return a + b[::-1] + c
