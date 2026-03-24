#User function Template for python3
class Solution:    
    def countX(self,L,R,X):
        #code here
        count = 0
        for i in range(L+1,R):
            count += str(i).count(str(X))
        return count
