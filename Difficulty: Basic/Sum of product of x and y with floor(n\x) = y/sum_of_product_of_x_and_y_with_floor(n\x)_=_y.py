#User function Template for python3
import math
class Solution:
	def sumofproduct(self, n):
		# Code here
		result = 0
		for i in range(1,n+1):
		    result += i*math.floor(n/i)
        return result
