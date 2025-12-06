from collections import Counter

class Solution:
    def mostFreqEle(self, arr):
        freq = Counter(arr)
        max_count = 0
        result = float('-inf')
        for key, value in freq.items():
            if value > max_count or (value == max_count and key > result):
                max_count = value
                result = key
        return result
