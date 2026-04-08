class Solution:
    def sort012(self, arr):
        # code here
        count0 = arr.count(0)
        count1 = arr.count(1)
        count2 = arr.count(2)
        idx = 0
        for i in range(count0):
            arr[idx] = 0
            idx += 1
        for i in range(count1):
            arr[idx] = 1
            idx += 1
        for i in range(count2):
            arr[idx] = 2
            idx += 1
        return arr
