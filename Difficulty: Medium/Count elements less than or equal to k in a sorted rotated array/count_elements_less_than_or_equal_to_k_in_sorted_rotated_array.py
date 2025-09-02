class Solution:
    def countLessEqual(self, arr, x):
        #code here
        count = 0
        for i in arr:
            if x >= i:
                count += 1
        return count
