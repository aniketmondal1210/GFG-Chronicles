class Solution:
    # Function to count pairs of characters from array and string.
    def count_pairs(self, arr, s):
		#Complete the function
		count = 0
		for i in arr:
		    if i[0] in s and i[1] in s:
		        count += 1
	    return count
