class Solution:
    def countOnes(self, arr):
        #code here
        count = 0
        for i in arr:
            if i == 1:
                count += 1
        return count
