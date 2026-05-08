#User function Template for python3
class Solution:
	def is_power_of_eight(self, n):
		# Code here
		while n % 8 == 0:
		    n //= 8
		return "Yes" if n == 1 else "No"
