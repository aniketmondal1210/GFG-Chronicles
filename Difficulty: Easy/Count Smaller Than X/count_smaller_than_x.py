#User function Template for python3
class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        count = 0
        for i in arr:
            if x > i:
                count += 1
        return count
