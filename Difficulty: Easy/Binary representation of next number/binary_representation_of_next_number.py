#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
		a = int(s,2)
		return bin(a+1)[2:]
