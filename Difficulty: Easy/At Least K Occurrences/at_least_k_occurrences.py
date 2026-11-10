class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        # code here
        dictionary = {}
        for i in arr:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
            if dictionary[i] == k:
                return i
        return -1
