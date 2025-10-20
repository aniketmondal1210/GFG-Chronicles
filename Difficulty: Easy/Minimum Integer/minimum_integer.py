from typing import List
class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        A.sort()
        S = sum(A)
        for i in A:
            if S <= N*i:
                return i
