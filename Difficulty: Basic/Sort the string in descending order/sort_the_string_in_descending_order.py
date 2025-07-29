#User function Template for python3
class Solution:
    def ReverseSort(self, s): 
        # code here
        a = ''.join(sorted(s))
        return a[::-1]
