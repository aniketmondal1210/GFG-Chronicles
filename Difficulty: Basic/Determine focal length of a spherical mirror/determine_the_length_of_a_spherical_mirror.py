#User function Template for python3
import math
class Solution:
	def findFocalLength(self, R, type):
		# Code here
		if type == 'convex':
		    return math.floor(-R/2)
		return math.floor(R/2)
