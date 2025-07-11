from typing import List

class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        if arr[::-1] == arr:
            return True
        else:
            return False
