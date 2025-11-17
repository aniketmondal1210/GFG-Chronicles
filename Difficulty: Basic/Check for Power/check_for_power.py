#User function Template for python3
class Solution:
    def isPowerOfAnother (ob,X,Y):
        # code here 
        if X == 1:
            return Y == 1
        while Y % X == 0:
            Y //= X
        return Y == 1
