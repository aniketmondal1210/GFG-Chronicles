#User function Template for python3
class Solution:
	def binaryPreviousNumber(self, S):
		# code here
		a = int(S,2)
		return bin(a-1)[2:]
