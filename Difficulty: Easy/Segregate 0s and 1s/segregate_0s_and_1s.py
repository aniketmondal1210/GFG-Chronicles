#User function Template for python3
class Solution:
    def segregate0and1(self, arr):
        # code here
        a = arr.count(0)
        for i in range(a):
            arr[i] = 0
        for j in range(a,len(arr)):
            arr[j] = 1
        return arr


#User function Template for python3
class Solution:
    def segregate0and1(self, arr):
        # code here
        arr.sort()
        return arr
