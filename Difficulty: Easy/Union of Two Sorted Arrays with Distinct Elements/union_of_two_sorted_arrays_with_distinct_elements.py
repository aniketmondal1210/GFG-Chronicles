#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        set_a = set(a)
        set_b = set(b)
        a = list(set_a.union(set_b))
        return sorted(a)
