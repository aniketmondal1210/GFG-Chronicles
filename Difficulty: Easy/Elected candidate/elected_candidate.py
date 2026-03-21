#User function Template for python3
from collections import Counter
class Solution:
	def electionWinner(self, arr):
		# code here
		a = Counter(arr)
		b = max(a.values())
		for key,value in a.items():
		    if value == b:
		        return key
