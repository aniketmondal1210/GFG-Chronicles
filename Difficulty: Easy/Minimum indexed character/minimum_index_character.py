class Solution:
    def printMinIndexChar(self, S, patt):
		#Code here
		for i in S:
		    if i in patt:
		        return i
	    return "$"
