class Solution:
	def fascinating(self, n):
	    # code here
	    combined = str(n) + str(n * 2) + str(n * 3)
	    if len(combined) != 9:
            return False
        digits = set(combined)
        return digits == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
