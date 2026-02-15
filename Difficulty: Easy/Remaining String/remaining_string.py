#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		array = []
		for i in range(len(s)):
		    if s[i] == ch:
		        array.append(i)
	    if len(array) < count:
            return ""
	    a = array[count-1]
	    return s[a+1:]
