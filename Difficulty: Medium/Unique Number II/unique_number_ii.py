#User function Template for python3
from collections import Counter
class Solution:
	def singleNum(self, arr):
		# Code here
		result = []
		a = Counter(arr)
		for key, value in a.items():
		    if value < 2:
		        result.append(key)
		result.sort()
		return result
