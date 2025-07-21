#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		a = S.split()
		result = ""
		for i in a:
		    result += i[0]
		return result
