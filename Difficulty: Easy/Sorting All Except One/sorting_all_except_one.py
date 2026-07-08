class Solution:
    def sort_except_k(self, arr, k):
        # code here
        x = arr[k]
        del arr[k]
        arr.sort()
        arr.insert(k, x)
        return arr
