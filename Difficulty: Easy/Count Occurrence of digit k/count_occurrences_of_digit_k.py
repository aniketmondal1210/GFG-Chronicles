class Solution:
    def num(self, k, arr):
        # code here
        count = 0
        for num in arr:
            count += str(num).count(str(k))
        return count
