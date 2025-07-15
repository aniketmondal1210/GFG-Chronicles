#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
    	# code here 
    	result = []
    	for i in matrix:
    	    for j in i:
    	        if j == x:
    	            return True
    	return False
