class Solution:
    def sortBySetBitCount(self, arr):
        # code here
        def count_set_bits(n):
            return bin(n).count('1')
        arr.sort(key=lambda x: -count_set_bits(x))
        return arr
