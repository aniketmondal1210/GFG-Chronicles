#User function Template for python3
# arr1 number[] 
# arr2 number[] 
# return boolean
class Solution:
    def isIdentical(self, a, b):
        #Your code goes here.
        a.sort()
        b.sort()
        return a == b
