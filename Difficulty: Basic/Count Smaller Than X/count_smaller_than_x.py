#User function Template for python3
class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        return sum(1 for i in arr if i < x)
