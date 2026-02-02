#User function Template for python3
class Solution:
    def minValue(self, arr1, arr2):
        #code here
        summ = 0
        arr1.sort()
        arr2.sort(reverse=True)
        for i in range(len(arr1)):
            summ += arr1[i]*arr2[i]
        return summ
