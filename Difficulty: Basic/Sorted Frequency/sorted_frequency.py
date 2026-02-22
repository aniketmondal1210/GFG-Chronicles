#User function Template for python3
from collections import Counter
class Solution:
	def freqSorted(self, arr):
		# code here
		a = Counter(arr)
		for key,value in sorted(a.items()):
		    print(key,value)
