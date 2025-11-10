#User function Template for python3
class Solution:
    def logicalOperation (self, A, B, C, D, E, F):
        # code here 
        return (int((not A) and B) or int(C and D) or int(E and (not F)))
        # both return statements will produce same output
        return ((1-A)*B + C*D + E*(1-F))
