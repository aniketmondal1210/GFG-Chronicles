from typing import List
class Solution:
    def specialIntegers(self, n : int, arr : List[int]) -> int:
        # code here
        a = set(arr)
        count = 0
        for i in a:
            if i-1 in a and i+1 in a:
                count += 1
        return count
