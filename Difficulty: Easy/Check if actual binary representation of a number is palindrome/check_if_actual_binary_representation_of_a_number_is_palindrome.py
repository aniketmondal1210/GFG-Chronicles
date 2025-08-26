#User function Template for python3
class Solution:
	def binaryPalin (self, N):
		# Your Code Here
		a = bin(N)[2:]
		return 1 if a[::-1] == a else 0
