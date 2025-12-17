#User function Template for python3
class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		result = ''
		for i in S:
		    if i.isalpha():
		        result += i
	    return result if len(result) > 0 else -1
