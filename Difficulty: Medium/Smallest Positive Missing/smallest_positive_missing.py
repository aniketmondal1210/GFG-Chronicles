class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        num = 1
        for i in arr:
            if i == num:
                num += 1
            elif i > num:
                return num
                break
            else:
                continue
        return num
