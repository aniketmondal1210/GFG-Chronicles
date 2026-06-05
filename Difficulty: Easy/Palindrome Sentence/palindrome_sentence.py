class Solution:
	def isPalinSent(self, s):
		# code here
		new_s = ""
		for i in s:
		    if i.isalnum():
		        new_s += i
	    new_s = new_s.lower()
	    return new_s[::-1] == new_s
