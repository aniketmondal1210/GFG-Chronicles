#User function Template for python3
class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        arr.sort(reverse = True)
        return max(arr[0]*arr[-1]*arr[-2],arr[0]*arr[1]*arr[2])
