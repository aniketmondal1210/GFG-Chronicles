#User function Template for python3
class Solution:
	def findSum(self, n):
		# Code here
		even_nums = n//2
		odd_nums = n - even_nums
		return odd_nums*odd_nums,even_nums*(even_nums+1)
