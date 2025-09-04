#User function Template for python3
class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        arr1.extend(arr2)
        arr1.sort()
        a = len(arr1)
        return arr1[a//2]+arr1[(a//2)-1]
