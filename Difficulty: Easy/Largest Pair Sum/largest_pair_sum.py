from typing import List
class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        arr.sort(reverse = True)
        return arr[0] + arr[1]
