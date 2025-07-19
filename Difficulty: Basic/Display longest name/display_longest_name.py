class Solution:
    def longest(self, arr):
        # code here
        max = 0
        word = ""
        for i in arr:
            if len(i)>max:
                max = len(i)
                word = i
        return word
