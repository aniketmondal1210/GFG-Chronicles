#User function Template for python3
class Solution:
    #Function to return a list containing the intersection of two arrays.
    def scores(self, arr1, arr2):
        a = 0
        b = 0
        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                a += 1
            elif arr1[i] < arr2[i]:
                b += 1
            else:
                continue
        return [a,b]
