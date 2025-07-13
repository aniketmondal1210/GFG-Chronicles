#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		a = bin(n)[2:]
		return a.count('1')
