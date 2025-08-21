from collections import Counter
class Solution:
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        #Your code here
        count = 0
        a = Counter(arr)
        for key,values in a.items():
            if values > len(arr)//k:
                count += 1
        return count
