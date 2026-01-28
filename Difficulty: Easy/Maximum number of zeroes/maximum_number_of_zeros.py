class Solution:
    def maxZero(self, arr):
        max_zeros = -1
        result = ""
        for s in arr:
            zeros = s.count('0')
            if zeros > max_zeros:
                max_zeros = zeros
                result = s
            elif zeros == max_zeros:
                if len(s) > len(result) or (len(s) == len(result) and s > result):
                    result = s
        return result if max_zeros > 0 else -1
