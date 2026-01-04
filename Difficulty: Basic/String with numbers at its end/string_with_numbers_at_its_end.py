#User function Template for python3
class Solution:
	def isSame(self, s):
		# code here
		count = 0
		num = ''
		for i in s:
		    if i.isalpha():
		        count += 1
		    else:
		        num += i
	    return 1 if count == int(num) else 0
