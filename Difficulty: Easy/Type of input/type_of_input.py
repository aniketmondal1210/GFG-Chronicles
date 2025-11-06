#User function Template for python3
class Solution:
    def isFloat(self,str1):
        if('.' not in str1):
            return False
        for i in str1:
            if i=='.':
                continue
            if not i.isdigit():
                return False
        return True
        
    def FindInputType(self,str):
    	# Code here
    	if(str.isdigit()):
    	    return "int"
    	elif(self.isFloat(str)):
            return "float"
        elif(len(str)==1):
            return "char"
        else:
            return "string"
